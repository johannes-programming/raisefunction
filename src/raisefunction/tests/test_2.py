import unittest
from typing import *

from raisefunction import core

__all__ = ["Test2"]


class Test2(unittest.TestCase):
    def test_raises_given_exception_instance_without_cause(self: Self) -> None:
        cm: unittest._AssertRaisesContext[ValueError]
        exc: ValueError
        exc = ValueError("boom")

        with self.assertRaises(ValueError) as cm:
            core.raisefunction(exc)

        self.assertIs(cm.exception, exc)
        # When no explicit cause is given, __cause__ is normally None.
        # __context__ may or may not be set depending on context.
        self.assertIsNone(cm.exception.__cause__)

    def test_raises_given_exception_class_without_cause(self: Self) -> None:
        cm: unittest._AssertRaisesContext[ValueError]
        with self.assertRaises(ValueError) as cm:
            core.raisefunction(ValueError)

        self.assertIsInstance(cm.exception, ValueError)
        self.assertIsNone(cm.exception.__cause__)

    def test_raises_with_explicit_cause(self: Self) -> None:
        cause: RuntimeError
        cm: unittest._AssertRaisesContext[ValueError]
        exc: ValueError
        cause = RuntimeError("original")
        exc = ValueError("wrapped")

        with self.assertRaises(ValueError) as cm:
            core.raisefunction(exc, cause)

        self.assertIs(cm.exception.__cause__, cause)

    def test_raise_from_None(self: Self) -> None:
        cm: unittest._AssertRaisesContext[ValueError]
        exc: ValueError
        one: int
        zero: int

        exc = ValueError("no context")
        with self.assertRaises(ValueError) as cm:
            try:
                # Create a real context exception
                one = 1
                zero = 0
                one / zero
            except ZeroDivisionError:
                raise exc from None
        self.assertIsNone(cm.exception.__cause__)
        self.assertIsInstance(cm.exception.__context__, ZeroDivisionError)
        self.assertTrue(cm.exception.__suppress_context__)

    def test_raising_class_that_requires_args_produces_type_error(self: Self) -> None:
        class NeedsArg(Exception):
            def __init__(self: Self, msg: str) -> None:
                super().__init__(msg)

        cm: unittest._AssertRaisesContext[BaseException]
        with self.assertRaises(TypeError) as cm:
            core.raisefunction(NeedsArg)

        # Optional: sanity check on the error type/message
        self.assertIsInstance(cm.exception, TypeError)


if __name__ == "__main__":
    unittest.main()
