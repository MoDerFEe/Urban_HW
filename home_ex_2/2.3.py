a = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

j = 0
while j < len(a):
    if a[j] > 0:
        print(a[j])
        j += 1
    elif a[j] == 0:
        j += 1
    else:
        break
