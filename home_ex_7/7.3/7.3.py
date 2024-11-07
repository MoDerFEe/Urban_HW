from re import split


class WordsFinder:
    def __init__(self, *urls):
        self.file_names = list(urls)

    def get_all_words(self):
        all_words = {}
        pattern = r"[,\ \.\=\!\?\;\:\-\n]"
        for i in self.file_names:
            with open(i, 'r', encoding='utf-8') as file:
                words_line = []
                for line in file:
                    words = split(pattern, line.lower())
                    for wrd in words:
                        if wrd != '\n' and wrd != '':
                            words_line.append(wrd)
            all_words[i] = words_line
        self.all_words = all_words
        return self.all_words

    def find(self, word):
        ret = {}
        for i in self.all_words:
            k = 1
            for j in self.all_words[i]:
                if word.lower() == j:
                    ret[i] = k
                    return ret
                else:
                    k += 1
        return False

    def count(self, word):
        ret = {}
        for i in self.all_words:
            k = 0
            for j in self.all_words[i]:
                if word.lower() == j:
                    k += 1
            ret[i] = k
        return ret


if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt', 'Mother Goose - Monday’s Child.txt', 'Rudyard Kipling - If.txt',
                          'Walt Whitman - O Captain! My Captain!.txt', 'Результат (несколько файлов).txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('text'))  # 4 слова teXT в тексте всего
