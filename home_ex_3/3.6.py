data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
summ = 0


def calculate_structure_sum(data):
    global summ
    if type(data) == str:
        summ += len(data)
    elif type(data) == int or type(data) == float:
        summ += data
    else:
        for i in data:
            if type(i) == dict:
                for j in i.keys():
                    calculate_structure_sum(j)
                    calculate_structure_sum(i[j])
            else:
                calculate_structure_sum(i)

    return summ


print(calculate_structure_sum(data_structure))
