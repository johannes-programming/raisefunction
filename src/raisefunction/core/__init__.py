__all__ = ["raisefunction"]


def raisefunction(error: BaseException, /) -> None:
    "This function raises the error passed to it."
    raise error
