from typing import *

__all__ = ["raisefunction"]

DEFAULT = object()


@overload
def raisefunction(
    exc: BaseException | type[BaseException],
) -> Never: ...
@overload
def raisefunction(
    exc: BaseException | type[BaseException],
    cause: Optional[BaseException],
) -> Never: ...


def raisefunction(
    exc: BaseException | type[BaseException],
    cause: Optional[BaseException] | object = DEFAULT,
) -> Never:
    "This function raises the given exception."
    if cause is DEFAULT:
        raise exc
    else:
        raise exc from cause
