class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return (f'{self.name}, {self.weight}, {self.category}')


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        with open(self.__file_name, 'r') as file:
            read = file.read()
            file.close()
        return read

    def add(self, *products):
        with open(self.__file_name, 'a') as file:
            for i in products:
                line = f'{i.name}, {i.weight}, {i.category}'
                with open(self.__file_name, 'r') as file_exc:
                    if f'{line}' in file_exc.read():
                        print(f'Продукт {line} уже есть в магазине')
                    else:
                        file.write(f'{line}\n')
                    file_exc.close()
        file.close()


if __name__ == '__main__':
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())
