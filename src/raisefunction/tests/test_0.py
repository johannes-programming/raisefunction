from __future__ import annotations

__all__: list[str] = ["Test0"]

import unittest
from typing import Any, Self

from raisefunction.core import raisefunction


class Test0(unittest.TestCase):
    def test_dispatcher_no_arguments(self: Self, /) -> None:
        "Test the dispatcher raises a TypeError with no arguments."
        with self.assertRaises(TypeError):
            raisefunction()  # type: ignore[call-overload]
        # self.assertIn("requires at least 1 positional argument", str(context.exception))

    def test_dispatcher_too_many_arguments(self: Self, /) -> None:
        "Test the dispatcher raises a TypeError with more than 2 arguments."
        with self.assertRaises(TypeError):
            raisefunction(1, 2, 3)  # type: ignore[call-overload]
        # self.assertIn("takes at most 2 positional arguments", str(context.exception))

    def test_raise_single_exception(self: Self, /) -> None:
        "Test the single exception raising overload."
        with self.assertRaises(ValueError):
            raisefunction(ValueError("Test single exception"))

    def test_raise_exception_with_cause_0(self: Self, /) -> None:
        "Test the exception raising overload with a cause."
        assertion: Any
        with self.assertRaises(ValueError) as assertion:
            raisefunction(
                ValueError("Test exception"), TypeError("Cause exception")
            )
        self.assertEqual(str(assertion.exception), "Test exception")
        self.assertIsInstance(assertion.exception.__cause__, TypeError)
        self.assertEqual(str(assertion.exception.__cause__), "Cause exception")

    def test_invalid_arguments_in_overloads(self: Self, /) -> None:
        "Test invalid argument types raise appropriate errors."
        with self.assertRaises(TypeError):
            raisefunction("not an exception")  # type: ignore[call-overload]
        with self.assertRaises(TypeError):
            raisefunction("not an exception", "not a cause")  # type: ignore[call-overload]

    def test_raise_exception_with_cause(self: Self, /) -> None:
        "Test the exception raising overload with a cause."
        assertion: Any
        with self.assertRaises(ValueError) as assertion:
            raisefunction(
                ValueError("Test exception"), KeyError("Cause exception")
            )
        self.assertEqual(str(assertion.exception), "Test exception")
        self.assertIsInstance(assertion.exception.__cause__, KeyError)


if __name__ == "__main__":
    unittest.main()
