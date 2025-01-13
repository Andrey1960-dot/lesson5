import unittest
import module_12_3 as tests


testST = unittest.TestSuite()
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests.RunnerTest))
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(testST)
