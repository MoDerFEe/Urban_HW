import time
from threading import Thread as th


def write_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i + 1}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


st = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
et = time.time()
res = (time.strftime('%H:%M:%S', time.gmtime(time.time() - st)))
print(f'Работа потоков: {res}')

st = time.time()
thread1 = th(target=write_words, args=(10, 'example5.txt'))
thread2 = th(target=write_words, args=(30, 'example6.txt'))
thread3 = th(target=write_words, args=(200, 'example7.txt'))
thread4 = th(target=write_words, args=(100, 'example8.txt'))
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread3.join()
res = (time.strftime('%H:%M:%S', time.gmtime(time.time() - st)))
print(f'Работа потоков: {res}')
