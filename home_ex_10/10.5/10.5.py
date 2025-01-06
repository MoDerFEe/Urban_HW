import multiprocessing as mp
import time


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        for line in file:
            if line == '':
                break
            else:
                all_data.append(line)


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    start = time.time()
    for i in filenames:
        read_info(i)
    print(time.time() - start)

    start = time.time()
    with mp.Pool() as p:
        p.map(read_info, filenames)
    print(time.time() - start)
