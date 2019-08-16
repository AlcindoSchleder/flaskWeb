# -*- coding: utf-8 -*-
from unittest import TestCase

from workspaces.home.service import ValidationInput as VI

class TestInput(TestCase):

    def test_CheckStringValue(self):
        vi = VI()
        self.assertEqual(vi.CheckStringValue('121426')['status'], 401)
        self.assertEqual(vi.CheckStringValue('523563')['status'], 200)
        self.assertEqual(vi.CheckStringValue('552523')['status'], 401)
        self.assertEqual(vi.CheckStringValue('112233')['status'], 200)
        self.assertEqual(vi.CheckStringValue('AG7688')['status'], 401)
        self.assertEqual(vi.CheckStringValue('543F67')['status'], 401)
        self.assertEqual(vi.CheckStringValue('1987878')['status'], 401)
        self.assertEqual(vi.CheckStringValue('002398')['status'], 401)

# run test
if __name__ == '__main__':
    unittest.main()