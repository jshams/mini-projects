from levenshtein import levenshtein


class BKNode():
    def __init__(self, word):
        '''
        Instantiate a BKnode with a word and a dictionary to store its
        children.
        '''
        self.word = word
        self.children = {}

    def add_child(self, new_word):
        '''
        To add a child, find the distance between self's word and the new word.
        If this distance exists in this node's children, recurse on that child,
        otherwise, create a node of this word and add it as a child.
        '''
        word_dist = self.distance(new_word)

        # if a child with this distance does not exist add it
        if word_dist not in self.children:
            self.children[word_dist] = BKNode(new_word)
        # otherwise recursively call add_child to the child node
        else:
            self.children[word_dist].add_child(new_word)

    def distance(self, other_word):
        '''
        Using levenshtein distance, calculate the difference between this word
        and another given word.
        '''
        return levenshtein(self.word, other_word)

    def get_nearest_children(self, other_word, tollerance, dist=None):
        '''
        This method is used to find the children of this node that are
        potentially within the tollerance of the given word. This is done
        by finding the distance from this word to the other, well call that
        dist. Then all children of this node that are in range of
        (dist - tollerance, dist + tollerance) inclusive are returned in a
        list.
        '''
        if dist is None:
            dist = self.distance(other_word)

        nearest_children = []
        for n in range(dist - tollerance, dist + tollerance + 1):
            child = self.children.get(n)
            if child is not None:
                nearest_children.append(child)

        return nearest_children


class BKTree():
    '''
    BKTrees are a tree used for storing words by distance to their parents.
    They are especially useful for autocorrect algorithms.
    '''

    def __init__(self, words=None):
        self.root = None

        if words is not None:
            i = 0
            tenth = len(words) // 10
            if tenth == 0:
                tenth = 1
            for word in words:
                i += 1
                if i % tenth == 0:
                    print(f'{i / tenth * 10}%')
                self.insert(word)

    def insert(self, word):
        '''
        Insert a word into this tree by calling add_child to the root node.
        '''
        if self.root is None:
            self.root = BKNode(word)
        else:
            self.root.add_child(word)

    def nearest_word_search(self, word, tollerance=3):
        '''
        Traverse this tree by finding all nearest children of each node that
        fall within the tollerance of the word. Returns a list of all words
        that are of the minimum edit distance to the given word.
        '''
        node = self.root

        # store a dictionary mapping distances to lists of words that are
        # of that distance to the given word
        possible_neighbors = {}

        # use a stack for DFS traversal
        stack = [node]
        # keep track of the number of traversals for benchmarking
        num_traversed = 0

        # traverse using DFS
        while len(stack) > 0:
            node = stack.pop()
            dist = node.distance(word)
            if dist == 0:
                return [node.word]

            # add a word to possible neighbors if its distance is less than tol
            if dist <= tollerance:
                possible_neighbors.setdefault(dist, []).append(node.word)

            # get the node's tollerable children and add them to the stack
            children = node.get_nearest_children(word, tollerance, dist=dist)
            num_traversed += len(children)
            stack.extend(children)

        # if there are no possible neightbors, no words fall within this word's
        # tollerance
        if len(possible_neighbors) == 0:
            return []

        # uncomment below to print num traversals for benchmarking
        # print(f'Num traversals: {num_traversed}')

        # return the list of words with the smallest distance from the word
        closest_dist = min(possible_neighbors.keys())
        return possible_neighbors[closest_dist]


def _save_new_bk_tree(pkl_file_name):
    '''
    Creates and saves a BKTree from built in list of English words to a .pkl
    file.
    '''
    from pickle import dump
    from random import shuffle

    # text file containing 235886 english words
    f = open('/usr/share/dict/words')
    words = f.read().splitlines()

    # important the the words are shuffled before insertion.
    # we don't want an unbalanced tree
    shuffle(words)

    print('Building Tree')
    bk_tree = BKTree(words=words)

    pkl_file = open(pkl_file_name, 'wb+')

    dump(bk_tree, pkl_file)
    print(f'Tree saved to "{pkl_file_name}".')

    return bk_tree


def _load_bk_tree(pkl_file_name):
    '''
    Loads a BKTree from a saved .pkl file.
    '''
    from pickle import load

    pkl_file = open(pkl_file_name, 'rb')
    bk_tree = load(pkl_file)

    return bk_tree


def load_or_save_bk_tree(pkl_file='autocorrect-tree.pkl'):
    '''
    Using the two functions above, load or save a BK tree depenfind on whether
    or not the .pkl file specified exists. Returns the created or loaded BK
    tree.
    '''
    from os.path import isfile

    if isfile(pkl_file):
        # load bk tree and time it
        start = time()
        bk_tree = _load_bk_tree(pkl_file)
        duration = round(time() - start, 3)
        print(f'Time to load tree: {duration} seconds')
    else:
        # create and save bk tree and time it
        start = time()
        bk_tree = _save_new_bk_tree(pkl_file_name=pkl_file)
        duration = round(time() - start, 3)
        print(f'Time to create tree: {duration} seconds')

    return bk_tree


if __name__ == '__main__':
    from time import time
    pkl_file = 'autocorrect-tree.pkl'
    bk_tree = load_or_save_bk_tree(pkl_file)

    word = 'lemoon'
    tol = 1

    # search for a word and time it
    start = time()
    res = bk_tree.nearest_word_search(word, tollerance=tol)
    duration = round(time() - start, 1)
    print(f'Time to search for word with tollerance of {tol}: '
          f'{duration} seconds')
    print(res)
