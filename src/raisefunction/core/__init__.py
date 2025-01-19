from typing import *

from overloadable import overloadable

__all__ = ["raisefunction"]


@overloadable
def raisefunction(*args: Any, **kwargs: Any) -> int:
    "This function works as dispatcher."
    argc = len(args)
    keys = set(kwargs.keys())
    if argc <= 1 and keys == set():
        return 1
    if argc == 0 and keys == {"exc"}:
        return 1
    return 2


@raisefunction.overload(1)
def raisefunction(exc: BaseException) -> None:
    "This function raises the given exception."
    raise exc


@raisefunction.overload(2)
def raisefunction(exc: BaseException, cause: Optional[BaseException]) -> None:
    "This function raises the given exception with the given cause."
    raise exc from cause
