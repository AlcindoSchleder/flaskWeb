# -*- coding: utf-8 -*-
import unittest
from workspaces.home.service import ValidationInput

class TestInput(unittest.TestCase):

    def test_CheckStringValue(self):
        Val = ValidationInput()
        self.assertEqual(Val.CheckStringValue('121426')['status'], 401)
        self.assertEqual(Val.CheckStringValue('523563'), True)
        self.assertEqual(Val.CheckStringValue('552523'), False)
        self.assertEqual(Val.CheckStringValue('112233'), True)
        self.assertEqual(Val.CheckStringValue('AG7688'), False)
        self.assertEqual(Val.CheckStringValue('543F67'), False)
        self.assertEqual(Val.CheckStringValue('1987878'), False)
        self.assertEqual(Val.CheckStringValue('002398'), False)

# run test
if __name__ == '__main__':
    unittest.main()