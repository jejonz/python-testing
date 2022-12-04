#!/usr/bin/env python3
import unittest
from external_function import function_to_test

from unittest import mock

class testExternalFunctionUsingPatch(unittest.TestCase):

    @mock.patch('external_function.external_dependency')
    def test_mock(self, mock_external_dependency):

        mock_external_dependency.return_value = True
        
        result = function_to_test()

        self.assertTrue(result)
    
if __name__ == '__main__':
    unittest.main()
