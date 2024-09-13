calls = 0


def count_calls():
    global calls
    calls += 1


def is_contains(string, list_to_search):
    count_calls()
    if string.lower() in list_to_search:
        return True
    else:
        return False


def string_info(word):
    count_calls()
    mass = (len(word), word.upper(), word.lower())
    return mass


try:
    k = int(input('Повторить раз: '))
    for i in range(k):
        a = str(input('Слово: '))
        print(string_info(a))
    for i in range(k):
        a = str(input('Слово: '))
        l = int(input('Слов в словаре: '))
        mass = []
        for j in range(l):
            mass.append((str(input(f'{j + 1} слово в словаре: '))).lower())
        print(is_contains(a, mass))
    print(calls)
except:
    False
