import unittest

from raisefunction.core import raisefunction


class TestRaiseFunction(unittest.TestCase):

    def test_raise_value_error(self):
        """Test if raisefunction raises a ValueError as expected."""
        with self.assertRaises(ValueError) as context:
            raisefunction(ValueError("This is a ValueError"))
        self.assertEqual(str(context.exception), "This is a ValueError")

    def test_raise_type_error(self):
        """Test if raisefunction raises a TypeError as expected."""
        with self.assertRaises(TypeError) as context:
            raisefunction(TypeError("This is a TypeError"))
        self.assertEqual(str(context.exception), "This is a TypeError")

    def test_raise_custom_exception(self):
        """Test if raisefunction raises a custom exception as expected."""

        class CustomError(Exception):
            pass

        with self.assertRaises(CustomError) as context:
            raisefunction(CustomError("This is a CustomError"))
        self.assertEqual(str(context.exception), "This is a CustomError")


if __name__ == "__main__":
    unittest.main()
