class WordsFinder:
    all_words = {}
    def __init__(self, *files):
        self.files = files
    def get_all_words(self):

        pun = [',', '.', '=', '!', '?', ';', ':', ' - ']
        words = []
        for i in self.files:
            with open(i, encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    line_new = ''
                    for j  in line:
                        if j not in pun:
                            line_new += j
                    line_new = line_new.split()
                    for k in line_new:
                        words.append(k)
            self.all_words[i] = words
        return self.all_words
    def find(self, word):
        dict_find = {}
        word = word.lower()
        for k, v in self.all_words.items():
            if word in v:
                dict_find[k] = v.index(word)+1
        return dict_find
    def count(self, word):
        dict_find = {}
        c = 0
        word = word.lower()
        for k, v in self.all_words.items():
            if word in v:
                c += 1
                dict_find[k] = v.count(word)
        return dict_find
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))