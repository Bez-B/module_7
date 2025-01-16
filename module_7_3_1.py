import string

class WordsFinder:
    """
    Класс поиска слов
    """

    def __init__(self, *args):
        self.file_names = list(args)  # Объект класса принимает названия файлов и записывает их в атрибут в виде списка.
        self.all_words = {}

    def get_all_words(self):
        """
        Подготовительный метод, который возвращает словарь следующего вида:
        {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
        """


        for i in self.file_names:
            with (open(i, encoding='utf-8') as file):
                for line in file:
                    s = line.lower().translate(str.maketrans('', '', string.punctuation))
                    s = s.rstrip()
                    list_words = s.split()
                    self.all_words[i] = list_words
        print(self.all_words)
        return self.all_words

    def get_all_words2(self):
        """
        Подготовительный метод, который возвращает словарь следующего вида:
        {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
        """

        for i in self.file_names:
            with (open(i, encoding='utf-8') as file):
                list_1 = []
                for line in file:
                    s = line.lower().translate(str.maketrans('', '', string.punctuation))
                    s = s.rstrip()
                    list_1.append(s)
                    self.all_words[i] = list_1
        print(self.all_words)

    def find(self, word):
        pass

    def count(self, word):
        pass

    def __str__(self):  # Для самопроверки правильности создания объекта
        return f'файлы {self.file_names}'


L1 = WordsFinder('file1.txt', 'file2.txt', 'file3.txt', 'file4.txt')

L1.get_all_words()

L1.get_all_words2()
