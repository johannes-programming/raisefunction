import unittest

from raisefunction.core import raisefunction


class TestRaiseFunction(unittest.TestCase):

    def test_raise_exception_with_cause(self):
        """Test the exception raising overload with a cause."""
        with self.assertRaises(ValueError) as context:
            raisefunction(ValueError("Test exception"), KeyError("Cause exception"))
        self.assertEqual(str(context.exception), "Test exception")
        self.assertIsInstance(context.exception.__cause__, KeyError)


if __name__ == "__main__":
    unittest.main()
