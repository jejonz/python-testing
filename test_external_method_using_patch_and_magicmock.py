#!/usr/bin/env python3
import unittest
from unittest import mock

from external_method import ExternalMethodTest

class testExternalMethodUsingPatch(unittest.TestCase):

    @mock.patch(
        'external_method.ExternalMethodTest.internal_method', mock.MagicMock(return_value=True)
    )
    def test_method_using_patch_decorator(self):
        obj = ExternalMethodTest()
        result = obj.method_to_test()

        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
