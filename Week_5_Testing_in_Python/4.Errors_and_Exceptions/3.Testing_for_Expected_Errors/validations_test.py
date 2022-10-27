from validations import validate_user
import unittest


class TestValidateUser(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validate_user("validUser", 3), True)

    def test_too_shot(self):
        self.assertEqual(validate_user("inv", 5), False)

    def test_invalid_characters(self):
        self.assertEqual(validate_user("invalid_User", 1), False)

    def test_invalid_minlen(self):
        self.assertRaises(ValueError, validate_user, "user", -1)


unittest.main()
