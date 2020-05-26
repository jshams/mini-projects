class Node():
    def __init__(self, letter):
        self.letter = letter
        self.children = dict()
        self.terminal = False

    def __hash__(self):
        return hash(self.letter)

    def __eq__(self, other):
        return self.letter == other.letter

    def __len__(self):
        return len(self.children)

    def add_child(self, letter):
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
        for word in word_list:
            self.add_word(word.lower())

    def add_word(self, word):
        first_letter = True
        node = None
        for letter in word:
            if first_letter:
                node = self.root[letter]
                first_letter = False
            else:
                node.add_child(letter)
                node = node.children[letter]
        node.children['end'] = None

    def _get_final_node(self, prefix):
        first_letter = True
        if prefix == '':
            return None
        for letter in prefix:
            if not letter.isalpha():
                return None
            if first_letter:
                node = self.root[letter]
                first_letter = False
            else:
                if letter in node.children:
                    node = node.children[letter]
                else:
                    return None
        return node

    def _get_all_children(self, node, prefix):
        all_combos = []
        for child in node.children:
            if child == 'end':
                all_combos.append(prefix)
            else:
                all_combos.extend(self._get_all_children(
                    node.children[child], prefix + child))
        return all_combos

    def auto_complete(self, prefix):
        prefix = prefix.lower()
        node = self._get_final_node(prefix)
        if node is None:
            return []
        words = self._get_all_children(node, prefix)
        return words


class AutoComplete():
    def __init__(self, dict_path='/usr/share/dict/words'):
        self.word_count = 0
        self.word_list = self.get_words_from_file(dict_path)
        self.trie_tree = Trie(self.word_list)

    def get_words_from_file(self, dict_path):
        f = open(dict_path)
        word_list = []
        for word in f.readlines():
            word_list.append(word.strip())
            self.word_count += 1
        return word_list

    def auto_complete(self, prefix):
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
