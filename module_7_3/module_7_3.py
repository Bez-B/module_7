import string

class WordsFinder:
    """
    Класс поиска слов
    """

    def __init__(self, *args):
        self.file_names = list(args)  # Объект класса принимает названия файлов и записывает их в атрибут в виде списка.
        self.all_words = {}           # Словарь для метода get_all_words
        self.word = None              # Искомое слово предаваемое в метод find
        self.words_place = {}         # Словарь для метода find
        self.num_words = {}           # Словарь для метода count


    def get_all_words(self):
        """
        Подготовительный метод, который возвращает словарь следующего вида:
        {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
        """

        for i in self.file_names:
            with (open(i, encoding='utf-8') as file):
                list_words = []
                for line in file:
                    s = line.lower().translate(str.maketrans('', '', string.punctuation))
                    s = s.rstrip()
                    list_s = s.split()
                    for j in list_s:
                        list_words.append(j)
                self.all_words[i] = list_words
        return self.all_words


    def find(self, word):
        """
        Метод, где word - искомое слово. Возвращает словарь, где ключ - название файла,
        значение - позиция первого такого слова в списке слов этого файла.
        """

        self.get_all_words()
        self.word = word.lower()
        for key, values in self.all_words.items():
            if self.word in values:
                place = values.index(self.word) + 1
                self.words_place[key] = place
        return self.words_place


    def count(self, word):
        """
        Метод, где word - искомое слово.
        Возвращает словарь, где ключ - название файла, значение - количество слов word в списке слов этого файла.
        """

        self.get_all_words()
        self.word = word.lower()
        for key, values in self.all_words.items():
            if self.word in values:
                num = values.count(self.word)
                self.num_words[key] = num
        return self.num_words

    def __str__(self):  # Для самопроверки правильности создания объекта
        return f'файлы {self.file_names}'


finder2 = WordsFinder('file1.txt', 'file2.txt', 'file3.txt', 'file4.txt')
print(finder2.get_all_words())
print(finder2.find('WORD10'))
print(finder2.count('WORD10'))
