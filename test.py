# -*- coding: utf-8 -*-
import unittest
from workspaces.home.service import ValidationInput

class TestInput(unittest.TestCase):

    def test_CheckStringValue(self):
        Val = ValidationInput()
        self.assertEqual(Val.CheckStringValue('121426')['status'], 401)
        self.assertEqual(Val.CheckStringValue('523563')['status'], 200)
        self.assertEqual(Val.CheckStringValue('552523')['status'], 401)
        self.assertEqual(Val.CheckStringValue('112233')['status'], 200)
        self.assertEqual(Val.CheckStringValue('AG7688')['status'], 401)
        self.assertEqual(Val.CheckStringValue('543F67')['status'], 401)
        self.assertEqual(Val.CheckStringValue('1987878')['status'], 401)
        self.assertEqual(Val.CheckStringValue('002398')['status'], 401)

# run test
if __name__ == '__main__':
    unittest.main()