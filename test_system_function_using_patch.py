#!/usr/bin/env python3
import unittest

from unittest import mock

from external_function import function_to_test_using_math

class testExternalFunctionUsingPatch(unittest.TestCase):

    def test_without_patch(self):

        result = function_to_test_using_math(4)

        self.assertEqual(result, 2.0)

    @mock.patch('external_function.sqrt')
    def test_with_patch(
        self,
        mock_sqrt
    ):
        mock_sqrt.return_value = 99.0
        
        result = function_to_test_using_math(4)

        self.assertEqual(result, 99.0)
    
if __name__ == '__main__':
    unittest.main()
