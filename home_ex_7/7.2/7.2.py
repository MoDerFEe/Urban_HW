def custom_write(file_name, strings):
    dict = {}
    j = 0
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in strings:
            j += 1
            dict[(j, file.tell())] = i
            file.write(f'{i}\n')
        file.close()
    return dict


if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)
