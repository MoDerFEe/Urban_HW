my_dict= {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print(my_dict)
print(my_dict.get('Vasya'))
print(my_dict.get('Joka'))
my_dict.update(
    {
        'Boka':2013,
        'Joka':2001
    }
)
print(my_dict.pop('Egor'))
print(my_dict)

my_set = {1, 'Joka', True, 2.13}
print(my_set)
my_set.update({5,6})
my_set.remove(1)
print(my_set)
