import unittest
'''
the file in /tests/homework/b_in_proc_out/tests_in_proc_out
has the test functions
'''
#from tests.examples.d_repetition.repitition import sum_of_squares, test_config
#from tests.examples.a_example import tests_devprocess
from tests.homework.c_decisions import tests_decisions


suite = unittest.TestLoader().loadTestsFromModule(tests_decisions)
unittest.TextTestRunner(verbosity=2).run(suite)
