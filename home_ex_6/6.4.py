import math


class Figure:

    def __init__(self, sides, color, field=True):
        self.__sides = sides
        self.__color = list(color)
        self.field = field

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 < (r or g or b) < 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b) == 1:
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        for i in sides[0]:
            if i <= 0 or len(sides) != self.sides_count:
                return False
        return True

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides) == 1:
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, side):
        side = [side]
        super().__init__(side, color)
        self.__radius = side[0] / 2 / math.pi

    def get_square(self):
        return math.pi * (self.__radius ** 2)

    def __len__(self):
        return self.get_sides()[0]


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, side):
        side = [side]
        super().__init__(side, color)
        self.per = sum(self.__sides) / 2

    def get_square(self):
        x = self.per
        for i in range(self.sides_count):
            x *= self.per - self.__sides[i]
        return x ** 0, 5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side):
        side = [side] * self.sides_count
        super().__init__(side, color)

    def get_volume(self):
        side = super().get_sides()
        return side[0] ** 3


if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())
