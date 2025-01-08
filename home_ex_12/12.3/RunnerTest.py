from runner import *
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        test_1 = Runner('test_1')
        for i in range(10):
            test_1.walk()
        self.assertEqual(test_1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        test_2 = Runner('test_2')
        for i in range(10):
            test_2.run()
        self.assertEqual(test_2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        test_3 = Runner('test_3')
        test_4 = Runner('test_4')
        for i in range(10):
            test_3.run()
            test_4.walk()
        self.assertNotEqual(test_3.distance, test_4.distance)


if __name__ == '__main__':
    unittest.main()
