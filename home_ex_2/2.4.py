a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

p = []
np = []

for i in a:
    if i == 0:
        continue
    elif i == 2:
        p.append(i)
        continue
    for j in range(i):
        if j == 0 or j == 1:
            continue
        if i % j == 0:
            np.append(i)
            break
        if j == i - 1:
            p.append(i)

print(p)
print(np)
