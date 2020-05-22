class Anagrams():
    '''
    This Anagram class is used to generate anagrams.
    It works by creating a dictionary of all words where the keys are
    sorted words and the values are all anagrams of that sorted word.
    '''

    def __init__(self, all_words=None):
        '''
        initialize this anagram class with a list of specified words,
        or if all_words is None, use your user dictionary of words.
        '''
        self.all_anagrams = {}
        self._add_all_words(all_words)

    def _add_all_words(self, all_words):
        '''
        add all words to self. If all_words is None use usr/dict
        '''
        # grab all words from user dictionary
        if all_words is None:
            f = open('/usr/share/dict/words')
            all_words = f.read().splitlines()
            f.close()
        # add all word in all_words
        for word in all_words:
            self._add_word(word)

    def _add_word(self, word):
        '''
        add a single word to self.anagrams.
        Words are stored as sorted keys, and their values are an array of
        all anagrams.
        '''
        # sort the word to use as a key
        sorted_word = ''.join(sorted(word))
        # add this word to anagrams dictionary with the key being the sorted
        # word and value being an array of anagrams.
        # setdefault saves time by only hashing the key once
        # https://docs.python.org/2/library/stdtypes.html#dict.setdefault
        self.all_anagrams.setdefault(sorted_word, []).append(word)

    def get_anagrams(self, word):
        '''
        External method used after class is instantiated. Returns a list
        of all anagrams of a word, or an empty list is none exist.
        '''
        # sort the word to use as a key
        sorted_word = ''.join(sorted(word))
        # get the anagrams from self.all_anagrams
        anagrams = self.all_anagrams.get(sorted_word)
        # if no key exists, no anagrams exist
        if anagrams is None:
            # return an empty list
            return []
        else:
            # create a tuple of anagrams that don't include this word
            tuple_anagrams = tuple(gram for gram in anagrams if gram != word)
            return tuple_anagrams


if __name__ == '__main__':
    A = Anagrams()
    grams = A.get_anagrams('elmon')
    print(grams)
