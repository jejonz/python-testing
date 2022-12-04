#!/usr/bin/env python3
import unittest
from unittest import mock

from external_method import ExternalMethodTest

class testExternalMethodUsingMock(unittest.TestCase):

    def test_method(
        self,
    ):
        mock_internal_method = ExternalMethodTest.internal_method = mock.Mock()
        mock_internal_method.return_value = True
        
        obj = ExternalMethodTest()
        result = obj.method_to_test()

        self.assertTrue(result)
    
if __name__ == '__main__':
    unittest.main()
