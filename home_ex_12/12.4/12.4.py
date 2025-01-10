import logging
from rt_with_exceptions import *
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            test_1 = Runner('test_1')
            for i in range(10):
                test_1.walk()
            self.assertEqual(test_1.distance, -50)
            logging.info('"test_walk" выполнен успешно')
        except AssertionError as error:
            logging.warning(f'Неверная скорость для Runner \n{str(error)}', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            test_2 = Runner(['test_2', ])
            for i in range(10):
                test_2.run()
            self.assertEqual(test_2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as error:
            logging.warning(f'Неверный тип данных для объекта Runner \n{str(error)}', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        try:
            test_3 = Runner('test_3')
            test_4 = Runner('test_4')
            for i in range(10):
                test_3.run()
                test_4.walk()
            self.assertNotEqual(test_3.distance, test_4.distance)
            logging.info('"test_challenge" выполнен успешно')
        except AssertionError as error:
            logging.warning(f'Неверный тип данных для объекта Runner \n{str(error)}', exc_info=True)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                        format='%(asctime)s | %(levelname)s | %(message)s | %(module)s | %(funcName)s')
    unittest.main()
