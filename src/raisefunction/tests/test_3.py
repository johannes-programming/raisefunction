import unittest
from typing import *

from raisefunction import core

__all__ = ["Test3"]


class Test3(unittest.TestCase):

    def go(self: Self, *, use_func: bool) -> None:
        cm: unittest._AssertRaisesContext[ValueError]
        exc: ValueError
        exc = ValueError("no context")
        with self.assertRaises(ValueError) as cm:
            self.go_with(use_func=use_func, exc=exc)
        self.assertIsNone(cm.exception.__cause__)
        self.assertIsInstance(cm.exception.__context__, ZeroDivisionError)
        self.assertTrue(cm.exception.__suppress_context__)

    def go_with(self: Self, *, use_func: bool, exc: Exception) -> None:
        one: int
        zero: int
        try:
            # Create a real context exception
            one = 1
            zero = 0
            one / zero
        except ZeroDivisionError:
            # This should behave like: raise exc from None
            if use_func:
                core.raisefunction(exc, None)
            else:
                raise exc from None

    def test_raise_from_None(self: Self) -> None:
        self.go(use_func=False)
        self.go(use_func=True)


if __name__ == "__main__":
    unittest.main()
