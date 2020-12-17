import random
from parse_file import parse


class MarkovChain:
    def __init__(self, order=2, words=None, corpus=None):
        self.order = order

        self.chain = {}

        if words is not None:
            self.add_words(words)
        elif corpus is not None:
            words = parse(corpus)
            self.add_words(words)
        # self.handle_terminal_for_jony_ive_case()

    def add_words(self, words):
        prev = []
        for word in words:
            if len(prev) < self.order:
                prev.append(word)
                continue

            self._add_word(word, tuple(prev))

            prev.pop(0)
            prev.append(word)

        self._add_word(None, tuple(prev))

    def _add_word(self, word, prev):
        if prev in self.chain:
            if word in self.chain[prev]:
                self.chain[prev][word] += 1
            else:
                self.chain[prev][word] = 1
        else:
            self.chain[prev] = {word: 1}

    def handle_terminal_for_jony_ive_case(self):
        if self.order == 2:
            self.chain[('done', 'yet')] = {'at': 1}
        elif self.order == 3:
            self.chain[("haven't", 'done', 'yet')] = {'at': 1}
            self.chain[('done', 'yet', 'at')] = {'the': 1}

    def add_next_for_terminal(self, prev):
        if prev in self.chain:
            return

        prev = list(prev).pop(0)
        while len(prev) > 0:
            similar_prefixes = []
            for prefix in self.chain:
                if prefix[-len(prev):] == prev:
                    similar_prefixes.append(prefix)

            if len(similar_prefixes) > 0:
                combined_dict = {}

                for prefix in similar_prefixes:
                    for word, count in self.chain[prefix].items():
                        if word in combined_dict:
                            combined_dict[word] += count
                        else:
                            combined_dict[word] = count
                self.chain[prev] = combined_dict
                return

        self.chain[prev] = None

    def create_sentence(self, length):
        sentence_list = []
        start = random.choice(list(self.chain.keys()))

        sentence_list.extend(start[:length])

        for _ in range(self.order, length):

            prev = tuple(sentence_list[-self.order:])
            next_word = self.chose_random_word(prev)
            sentence_list.append(next_word)

        # capitalize the first word and add a . to the last
        sentence_list[0] = sentence_list[0].title()
        sentence_list[-1] += '.'

        return ' '.join(sentence_list)

    def chose_random_word(self, prev):
        next_words = self.chain[prev]

        sum_frequencies = sum(next_words.values())

        next_words_items = list(next_words.items())

        random_val = random.randint(1, sum_frequencies)

        i = 0
        while random_val > 0:
            random_val -= next_words_items[i][1]
            i += 1

        return next_words_items[i - 1][0]


if __name__ == '__main__':
    words = 'one fish two fish red fish blue fish two fish'.split(' ')
    mc = MarkovChain(order=2, words=words)
    # print(mc.chain)

    for i in range(5, 10):
        s = mc.create_sentence(i)
        print(s)
