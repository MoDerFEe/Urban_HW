def is_prime(func):
    def wrapper(*num):
        a = func(*num)
        for i in range(2, (a + 1) // 2):
            if a % i == 0:
                print('составное')
                return a
        print('простое')
        return a

    return wrapper


@is_prime
def sum_three(*num):
    return num[0] + num[1] + num[2]


if __name__ == '__main__':
    result = sum_three(2, 3, 6)
    print(result)
