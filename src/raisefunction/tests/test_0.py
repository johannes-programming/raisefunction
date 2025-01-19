import unittest

from raisefunction.core import raisefunction


class TestRaiseFunction(unittest.TestCase):
    def test_dispatcher_no_arguments(self):
        """Test the dispatcher raises a TypeError with no arguments."""
        with self.assertRaises(TypeError) as context:
            raisefunction()
        self.assertIn("requires at least 1 positional argument", str(context.exception))

    def test_dispatcher_too_many_arguments(self):
        """Test the dispatcher raises a TypeError with more than 2 arguments."""
        with self.assertRaises(TypeError) as context:
            raisefunction(1, 2, 3)
        self.assertIn("takes at most 2 positional arguments", str(context.exception))

    def test_raise_single_exception(self):
        """Test the single exception raising overload."""
        with self.assertRaises(ValueError):
            raisefunction(ValueError("Test single exception"))

    def test_raise_exception_with_cause(self):
        """Test the exception raising overload with a cause."""
        with self.assertRaises(ValueError) as context:
            raisefunction(ValueError("Test exception"), TypeError("Cause exception"))
        self.assertEqual(str(context.exception), "Test exception")
        self.assertIsInstance(context.exception.__cause__, TypeError)
        self.assertEqual(str(context.exception.__cause__), "Cause exception")

    def test_invalid_arguments_in_overloads(self):
        """Test invalid argument types raise appropriate errors."""
        with self.assertRaises(TypeError):
            raisefunction("not an exception")
        with self.assertRaises(TypeError):
            raisefunction("not an exception", "not a cause")


if __name__ == "__main__":
    unittest.main()
