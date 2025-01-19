from typing import *

from overloadable import overloadable

__all__ = ["raisefunction"]


@overloadable
def raisefunction(*args: Any) -> int:
    "This function works as dispatcher."
    if len(args) < 1:
        raise TypeError(
            "A raise statement requires at least 1 positional argument (0 given)."
        )
    if len(args) > 2:
        raise TypeError(
            "An assertion takes at most 2 positional arguments (%s given)." % len(args)
        )
    return len(args)


@raisefunction.overload(1)
def raisefunction(exc: BaseException, /) -> None:
    "This function raises the given exception."
    raise exc


@raisefunction.overload(2)
def raisefunction(exc: BaseException, cause: Optional[BaseException], /) -> None:
    "This function raises the given exception with the given cause."
    raise exc from cause
