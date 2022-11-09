from rearrange import rearrange_name
import unittest


class TestRearrange(unittest.TestCase):
    def testbasic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)


unittest.main()
