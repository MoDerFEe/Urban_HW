def print_params(a=1, b='строка', c=True):
    return a, b, c


# 1
print(print_params())
print(print_params(b=25))
print(print_params(c=[1, 2, 3]))

# 2
values_list = [2, 'Слово', False]
values_dict = {'a': 3, 'b': 'Символ', 'c': True}
print(print_params(*values_list))
print(print_params(**values_dict))

# 3
values_list_2 = [False, 'Знак']
print(print_params(*values_list_2, 42))