class Node():
    def __init__(self, letter):
        '''initialize a node with a letter as its letter'''
        self.letter = letter
        self.children = dict()
        self.terminal = False

    def add_child(self, letter):
        '''adds a child node containing letter, if it doesnt already exist'''
        if letter not in self.children:
            self.children[letter] = Node(letter)


class Trie():
    def __init__(self, word_list=None):
        self.root = dict([(letter, Node(letter))
                          for letter in 'abcdefghijklmnopqrstuvwxyz'])
        self.word_count = 0
        if word_list is not None:
            self.add_words(word_list)

    def add_words(self, word_list):
        '''add a list of words to this trie'''
        for word in word_list:
            self.add_word(word.lower())

    def add_word(self, word):
        '''add a single word to this trie'''
        node = None
        for letter in word:
            if node is None:
                node = self.root[letter]
            else:
                node.add_child(letter)
                node = node.children[letter]
        node.terminal = True

    def _get_final_node(self, prefix):
        '''given a prefix, walk this trie with the given prefix, and return
        the last node, or None if the walk is interrupted. Used by autocomplete
        method'''
        node = None
        if prefix == '':
            return None
        for letter in prefix:
            # make sure the string contains only letters
            if not letter.isalpha():
                return None

            if node is None:
                node = self.root[letter]
            else:
                if letter in node.children:
                    node = node.children[letter]
                else:
                    return None
        return node

    def _get_all_children(self, node, prefix, all_combos=None):
        '''returns a list of words that can be completed from a given node
        with an included prefix.
        Works by recursively searching children of each node.'''
        if all_combos is None:
            all_combos = []
        if node.terminal:
            all_combos.append(prefix)
        for letter, child_node in node.children.items():
            self._get_all_children(
                child_node, prefix + letter, all_combos)
        return all_combos

    def auto_complete(self, prefix):
        '''returns a list of words that can be completed bt a fiven prefix'''
        prefix = prefix.lower()
        node = self._get_final_node(prefix)
        if node is None:
            return []
        words = self._get_all_children(node, prefix)
        return words


class AutoComplete():
    '''
    AutoComplete class for completing words.
    '''

    def __init__(self, dict_path='/usr/share/dict/words'):
        self.word_count = 0
        self.word_list = self.get_words_from_file(dict_path)
        self.trie_tree = Trie(self.word_list)

    def get_words_from_file(self, dict_path):
        '''Reads words from a file and reurns them in a list'''
        f = open(dict_path)
        word_list = []
        for word in f.readlines():
            word_list.append(word.strip())
            self.word_count += 1
        return word_list

    def auto_complete(self, prefix):
        '''call this tries autocomplete with the prefix
        returns a list of words that complete the given prefix'''
        return self.trie_tree.auto_complete(prefix)


def main():
    from time import time, sleep
    # from termcolor import colored
    blue = '\x1b[94m'
    green = '\x1b[92m'
    yellow = '\x1b[93m'
    red = '\x1b[91m'
    end = '\033[0m'
    print(blue + 'Building trie...')
    start = time()
    ac = AutoComplete()
    print('Time to build trie:' + green, str(
        round(time() - start, 3)) + ' seconds')
    print(blue + 'Number of words:' + green, ac.word_count)
    while True:
        print(blue + 'Enter a lowercase prefix to find words with that prefix: ' +
              red + '(Q to quit)')
        pref = input(yellow)
        print('\033[0m')
        if pref == 'Q':
            print(red + 'Quitting...' + end)
            sleep(1)
            return
        else:
            words = ac.auto_complete(pref)
            print(green, ', '.join(words))
            print(blue)


if __name__ == '__main__':
    main()
