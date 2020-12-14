from queue import deque
from string import ascii_letters

letters = ascii_letters[:26]


class OutboundAutocorrect:
    '''
    The outbound approach for autocomplete works by storing a set of all word
    for fast lookup. A set of edits are performed using a BFS style. 1 edit at
    a time. When a layer of edits leads to an existing word, all real words
    found in that layer are returned.
    '''

    def __init__(self, words):
        self.letters = ascii_letters[:26]
        self.all_words = set(w.lower() for w in words)

    def additions(self, word):
        '''
        Given a word, generate all new words that can be created by adding
        all possible chars in every possible location.
        '''
        for char in self.letters:
            for i in range(len(word)):
                yield word[:i] + char + word[i:]

    def deletions(self, word):
        '''
        Given a word, generate all new words that can be created by deleting
        one char in the word.
        '''
        for i in range(len(word)):
            yield word[:i] + word[i + 1:]

    def substitutions(self, word):
        '''
        Given a word, generate all new words that can be created by
        substituting all possible chars in every possible location.
        '''
        for letter in self.letters:
            for i in range(len(word)):
                if letter != word[i]:
                    yield word[:i] + letter + word[i + 1:]

    def swaps(self, word):
        '''
        Given a word, generate all new words that can be created by swapping
        any two adjacent characters.
        '''
        for i in range(len(word) - 1):
            yield word[:i] + word[i + 1] + word[i] + word[i + 2:]

    def all_edits(self, word):
        '''
        Given a word, generate all words that are of edit distance 1 from word.
        '''
        yield from self.additions(word)
        yield from self.deletions(word)
        yield from self.substitutions(word)
        yield from self.swaps(word)

    def correct(self, word, tollerance=3):
        '''
        Using BFS search for all possible words that are possible real words
        that can be corrected from the given word with the minimun Edit
        Distance (aka Levenshtein Distance). Tollerace is the maximum Edit
        Distance to search for.


        Returns a tuple containing a list of words and an integer representing
        their edit distance.
        When 0 is returned as the dist, the given word already exists and has
        no typos.
        If no words are found within the given tollerance, an empty array along
        with the tollerance is returned.

        Time & space complexity:
        O((n * l) ** d) where n is the length of the word, d is the minimum
        distance to the next word and l is the number of new letters that can
        be used for editing.
        In the case that no correct word is found, d=tollerance. This is the
        worst case.
        In the case that the word exists already, the time is O(n), the
        amount of time it takes to lookup a string of length n in a set.
        This is the best case.
        '''
        # check if the word exists first
        if word in self.all_words:
            return [word], 0

        # declare distance as 1 indicating num edits from the original word
        distance = 1

        queue = deque()
        queue.append(word)

        # create a second queue to store next layer of edits
        # this is important for keeping track of the edit distance
        next_queue = deque()

        # create a list to store real words
        real_words = []

        # keep track of seen words to memoize/avoid repetition

        # This will omit some of the work, but not too much as the tree
        # becomes very wide very quickly.
        seen = set()

        # queue should contain typos, and next queue contains the next round
        # of typos.
        num_iters = 0
        # Continue searching until the max tollerance has been reached.
        while distance <= tollerance:

            if len(queue) == 0:
                # if any real words have been found, break the loop
                # to avoid a deeper search
                if len(real_words) > 0:
                    break
                # otherise, continue to the next layer by swapping the values
                # of queue and next_queue.
                # increment distance by 1 indicating another layer of search.
                queue, next_queue = next_queue, queue
                distance += 1

            word = queue.popleft()

            # find all words that can be created from 1 edit
            for edited_word in self.all_edits(word):
                num_iters += 1
                if edited_word in self.all_words:
                    real_words.append(edited_word)

                if edited_word not in seen:
                    # When real words has words or the distance=tollerance
                    # there will not be a next iteration, skip this step
                    if not (len(real_words) > 0 or distance == tollerance):
                        # add the next word
                        next_queue.append(edited_word)
                        seen.add(edited_word)

        print(num_iters)
        return real_words, distance


if __name__ == '__main__':
    f = open('/usr/share/dict/words')
    words = f.read().splitlines()
    s = OutboundAutocorrect(words)

    words, dist = s.correct('pooooooo')
    print(words)
    print(dist)
