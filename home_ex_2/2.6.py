from random import randint


def rnd(r):
    print(r)
    mas = []
    out = ''
    for i in range(1, r):
        for j in range(i + 1, r):
            if r % (i + j) == 0:
                mas.append([i, j])
    for i in range(len(mas)):
        out += (str(mas[i][0]) + str(mas[i][1]))
    return out


ans = rnd(randint(3, 20))
print(ans)
