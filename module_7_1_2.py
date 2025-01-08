class Product:
    """
    Класс продуктов
    """

    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    """
    Класс магазин
    """

    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        """
        Метод get_products считывает всю информацию из файла __file_name, закрывает его и возвращает единую строку
        со всеми товарами из файла __file_name.
        """
        file = open(self.__file_name, 'r')
        product_list = file.read()
        file.close()
        return f'{product_list}'

    def add(self, *products):
        """
        Метод add(self, *products) принимает неограниченное количество объектов класса Product.
        Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле
        (по полю name И по полю category). Если такой продукт уже есть, то увеличивает общий вес и выводит строку
        'Продукт <название> уже был в магазине, его общий вес теперь равен <вес>'.
        """
        for i in products:
            file = open(self.__file_name, 'r')
            f1 = file.read()
            file.close()
            if i.name not in f1 and i.category not in f1:
                file = open(self.__file_name, 'a')
                file.write(f'{str(i)}\n')
                file.close()
            # elif i.name in f1 and i.category in f1:
                # summ_weight = old_weight + i.weight
                # print(f'Продукт {i.name} уже был в магазине, его общий вес теперь равен {summ_weight} ')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

s1.add(p1, p2, p3)

print(s1.get_products())