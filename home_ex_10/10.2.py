import threading as th
import time


class Knight(th.Thread):
    def __init__(self, name, power):
        super().__init__(name=name)
        self.name = str(name)
        self.power = int(power)

    def run(self):
        enemy = 100
        print(f'{self.name} на нас напали!')
        j = 0
        while enemy > 0:
            time.sleep(1)
            enemy -= self.power
            j += 1
            if enemy < 0:
                enemy = 0
            print(f'{self.name} сражается {j} дней..., осталось {enemy} воинов.')
        print(f'{self.name} одержал победу спустя {j} дней(дня)!')


if __name__ == '__main__':
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)
    first_knight.start()
    second_knight.start()
    first_knight.join()
    second_knight.join()
    print('Все битвы закончились!')
