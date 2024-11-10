class Car:
    def __init__(self, model, __vin, __numbers):
        def __is_valid_vin(__vin):
            if 1000000 <= __vin <= 9999999 and isinstance(__vin, int):
                return True
            elif not isinstance(__vin, int):
                raise IncorrectVinNumber('Некорректный тип vin номер')
            else:
                raise IncorrectVinNumber('Неверный диапазон для vin номера')

        def __is_valid_numbers(__numbers):
            if len(__numbers) == 6 and type(__numbers) == str:
                return True
            elif type(__numbers) != str:
                raise IncorrectCarNumbers('Некорректный тип данных для номеров')
            else:
                raise IncorrectCarNumbers('Неверная длина номера')

        __is_valid_vin(__vin)
        __is_valid_numbers(__numbers)
        self.model = model
        self.__vin = __vin
        self.__numbers = __numbers


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
