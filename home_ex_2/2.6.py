from random import randint


def rnd(r):
    print(r)
    mas = []
    ans = ''
    for i in range(1, r):
        for j in range(i + 1, r):
            if r % (i + j) == 0:
                mas.append([i, j])
    for i in range(len(mas)):
        ans += (str(mas[i][0]) + str(mas[i][1]))
    return ans


print(rnd(randint(3, 20)))
