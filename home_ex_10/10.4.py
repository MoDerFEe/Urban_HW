import threading as th
from random import randint
from queue import Queue
import time


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(th.Thread):
    def __init__(self, name):
        super().__init__(name=name)
        self.name = name

    def run(self):
        time.sleep(randint(3, 10))

class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for i in guests:
            table = None
            for j in self.tables:
                if j.guest is None:
                    table = j
                    break
            if table:
                table.guest = i
                i.start()
                print(f'{i.name} сел(-а) за стол номер {table.number}')
            else:
                self.queue.put(i)
                print(f'{i.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty():
            for i in self.tables:
                if i.guest and not i.guest.is_alive():
                    print(f'{i.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {i.number} свободен')
                    i.guest = None
                if not self.queue.empty() and i.guest is None:
                    next_guest = self.queue.get()
                    i.guest = next_guest
                    next_guest.start()
                    print(f'{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {i.number}')
        while True:
            k = 0
            for i in self.tables:
                if i.guest is not None:
                    k = 1
                    break
            if not k:
                break
            for i in self.tables:
                if i.guest and not i.guest.is_alive():
                    print(f'{i.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {i.number} свободен')
                    i.guest = None

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
