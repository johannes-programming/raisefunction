from __future__ import annotations

__all__: list[str] = ["raisefunction"]

import enum
from typing import Never, overload


class Default(enum.Enum):
    DEFAULT = None


@overload
def raisefunction(
    exc: BaseException | type[BaseException],
) -> Never: ...
@overload
def raisefunction(
    exc: BaseException | type[BaseException],
    cause: BaseException | None,
) -> Never: ...


def raisefunction(
    exc: BaseException | type[BaseException],
    cause: BaseException | None | Default = Default.DEFAULT,
) -> Never:
    "This function raises the given exception."
    if isinstance(cause, Default):
        raise exc
    else:
        raise exc from cause
