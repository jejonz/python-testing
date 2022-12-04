#!/usr/bin/env python3
import unittest

from unittest import mock

class testMock(unittest.TestCase):

    def test_mock_object(self):
        # Create a test mock object
        test_mock = mock.Mock()
        test_mock.testMethod.return_value = 'test'
        
        # Call the test method
        test_mock.testMethod('input')
        
        # Assert called with correct input
        test_mock.testMethod.assert_called_with('input')
        test_mock.testMethod.assert_called_once_with('input')
    
if __name__ == '__main__':
    unittest.main()
