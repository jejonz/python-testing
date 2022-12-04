#!/usr/bin/env python3
import unittest
from unittest import mock

from external_method import ExternalMethodTest

class testExternalMethodUsingPatch(unittest.TestCase):

    def test_method_using_with(
        self,
    ):
        # Before the test
        obj = ExternalMethodTest()
        result = obj.method_to_test()

        self.assertFalse(result)

        with mock.patch('external_method.ExternalMethodTest.internal_method') \
            as mock_internal_class_dependency:
            # During the test
            mock_internal_class_dependency.return_value = True
            result = obj.method_to_test()

            self.assertTrue(result)

    @mock.patch('external_method.ExternalMethodTest.internal_method')
    def test_method_using_patch_decorator(
        self,
        mock_internal_class_dependency
    ):        
        mock_internal_class_dependency.return_value = True
        
        obj = ExternalMethodTest()
        result = obj.method_to_test()

        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
