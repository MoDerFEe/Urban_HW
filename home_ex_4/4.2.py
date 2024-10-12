def text():
    def inner():
        return 'Я в области видимости функции test_function'

    return inner()


print(text())

print(inner())