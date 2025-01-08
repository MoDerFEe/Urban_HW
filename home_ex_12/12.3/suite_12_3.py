import RunnerTest
import TournamentTest
import unittest

test = unittest.TestSuite()
test.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest.RunnerTest))
test.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest.TournamentTest))

run_test = unittest.TextTestRunner(verbosity=2)
run_test.run(test)
