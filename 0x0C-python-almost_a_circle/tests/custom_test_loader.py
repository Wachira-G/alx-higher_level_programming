#!/usr/bin/python3

"""A simple module used when the tear done and set up fail to cooperate
"""
import unittest

class CustomTestLoader(unittest.TestLoader):
    '''Loads unitests 
    '''
    def loadTestsFromModule(self, module, pattern=None):
        """loads unittests"""
        tests = super().loadTestsFromModule(module, pattern)
        for test_class in self.getTestCaseNames(module):
            tests.addTests(
                self.loadTestsFromTestCase(getattr(module, test_class)))
        return tests
