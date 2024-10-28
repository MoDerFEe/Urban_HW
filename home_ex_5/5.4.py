class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, floor):
        self.name = name
        self.floor = floor

    def __str__(self):
        return f'Название {self.name}, кол-во этажей {self.floor}'

    def __len__(self):
        return self.floor

    def __eq__(self, other):
        return self.floor == other.floor

    def __lt__(self, other):
        return self.floor < other.floor

    def __le__(self, other):
        return self.floor <= other.floor

    def __gt__(self, other):
        return self.floor > other.floor

    def __ge__(self, other):
        return self.floor >= other.floor

    def __ne__(self, other):
        return self.floor != other.floor

    def __add__(self, other):
        return House(self.name, self.floor + other)

    def __iadd__(self, other):
        self.floor += other
        return self

    def __radd__(self, other):
        return House(self.name, self.floor + other)

    def __del__(self):
        print(f'{self.name} снесен, но он останется в истории')
        del self


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
