class IncorrectType(Exception):
    def __init__(self, message):
        self.message = message


def apply_all_func(int_list, *functions):
    dict = {}
    for i in int_list:
        if not isinstance(i, (int, float)):
            raise IncorrectType(f'Некорректное значение {i}')
    for i in functions:
        dict[i.__name__] = i(int_list)

    return dict


if __name__ == '__main__':
    try:
        print(apply_all_func([6, 20, 15, 9], max, min))
        print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
    except IncorrectType as it:
        print(it.message)
