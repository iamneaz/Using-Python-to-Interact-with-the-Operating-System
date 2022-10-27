from rearrange import rearrange_name
import unittest


class TestRearrange(unittest.TestCase):
    def testBasic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)

    def testEmpty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)

    def test


unittest.main()
