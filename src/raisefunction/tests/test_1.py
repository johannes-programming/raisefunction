import unittest
from typing import *

from raisefunction import core

__all__ = ["Test1"]


class Test1(unittest.TestCase):
    def test_raises_given_exception_instance_without_cause(self: Self) -> None:
        exc: ValueError
        exc = ValueError("boom")

        with self.assertRaises(ValueError) as cm:
            core.raisefunction(exc)

        self.assertIs(cm.exception, exc)
        # When no explicit cause is given, __cause__ is normally None
        # and __context__ may or may not be set depending on context.
        self.assertIsNone(cm.exception.__cause__)

    def test_raises_given_exception_class_without_cause(self: Self) -> None:
        # Using a class mirrors: raise ValueError
        with self.assertRaises(ValueError) as cm:
            core.raisefunction(ValueError)
        self.assertIsInstance(cm.exception, ValueError)
        self.assertIsNone(cm.exception.__cause__)

    def test_raises_with_explicit_cause(self: Self) -> None:
        cause: RuntimeError
        exc: ValueError
        cause = RuntimeError("original")
        exc = ValueError("wrapped")

        with self.assertRaises(ValueError) as cm:
            core.raisefunction(exc, cause)

        self.assertIs(cm.exception.__cause__, cause)

    def test_raises_with_suppressed_context_when_cause_is_none(
        self: Self,
    ) -> None:
        exc: ValueError
        exc = ValueError("no context")

        # Explicit `from None` should result in __cause__ being None,
        # and suppress linking to any active exception.
        with self.assertRaises(ValueError) as cm:
            core.raisefunction(exc, None)

        self.assertIsNone(cm.exception.__cause__)

    def test_raising_class_that_requires_args_produces_type_error(
        self: Self,
    ) -> None:
        class NeedsArg(Exception):
            def __init__(self: Self, msg: str) -> None:
                super().__init__(msg)

        # This mirrors normal `raise NeedsArg` behaviour
        with self.assertRaises(TypeError):
            core.raisefunction(NeedsArg)


if __name__ == "__main__":
    unittest.main()
