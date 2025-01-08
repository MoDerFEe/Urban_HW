"""
Ошибка в некорректной обработке дистанции и скоростей,
То есть необходимо производить сортировку объектов по пройденной дистанции,
что бы избежать ошибки, кто прошел большую дистанцию в следующий раз обрабатывается первым
Если этого не делать, и различие скоростей будет минимальным, а расстояние коротким, то
даже если первый бегун прошел меньшее расстояние, чем второй, но ему хватит дистанции+скорость*2
>= общая дистанция, он прибежит якобы первым.
Решение - не удалять бегунов из списка, а перемещать в отдельный список с пройденной дистанцией,
далее - отсортировать данный список по ключу "пройденная дистанция" и уже после этого присвоить места
"""

import unittest
from runner_and_tournament import *


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i, j in cls.all_results.items():
            print(j)

    def test_1(self):
        tour = Tournament(90, self.runner_1, self.runner_3)
        res = tour.start()
        self.__class__.all_results['test_1'] = {}
        for i, j in res.items():
            self.__class__.all_results['test_1'] = {**self.__class__.all_results.get('test_1'), **({i: str(j)})}
        self.assertEqual(str(j), 'Ник')

    def test_2(self):
        tour = Tournament(90, self.runner_2, self.runner_3)
        res = tour.start()
        self.__class__.all_results['test_2'] = {}
        for i, j in res.items():
            self.__class__.all_results['test_2'] = {**self.__class__.all_results.get('test_2'), **({i: str(j)})}
        self.assertEqual(str(j), 'Ник')

    def test_3(self):
        tour = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        res = tour.start()
        self.__class__.all_results['test_3'] = {}
        for i, j in res.items():
            self.__class__.all_results['test_3'] = {**self.__class__.all_results.get('test_3'), **({i: str(j)})}
        self.assertEqual(str(j), 'Ник')


if __name__ == '__main__':
    unittest.main()
