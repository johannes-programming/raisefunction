from __future__ import annotations

__all__: list[str] = ["Test3"]

import unittest
from typing import Any, Self

from raisefunction import core


class Test3(unittest.TestCase):

    def go(self: Self, /, *, use_func: bool) -> None:
        cm: Any
        exc: ValueError
        exc = ValueError("no context")
        with self.assertRaises(ValueError) as cm:
            self.go_with(use_func=use_func, exc=exc)
        self.assertIsNone(cm.exception.__cause__)
        self.assertIsInstance(cm.exception.__context__, ZeroDivisionError)
        self.assertTrue(cm.exception.__suppress_context__)

    def go_with(self: Self, /, *, exc: Exception, use_func: bool) -> None:
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

    def test_raise_from_None(self: Self, /) -> None:
        self.go(use_func=False)
        self.go(use_func=True)


if __name__ == "__main__":
    unittest.main()
