def all_variants(text):
    a, b = 0, 1
    while True:
        yield text[a:a + b]
        a += 1
        if a + b == len(text) + 1:
            a = 0
            b += 1
        if b == len(text) + 1:
            break


a = all_variants("abc")
for i in a:
    print(i)
