from typing import Final, Never, Optional, cast, overload

__all__ = ["raisefunction"]

DEFAULT: Final[object] = object()


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
        raise exc from cast(Optional[BaseException], cause)
