from __future__ import annotations

__all__: list[str] = ["main"]

import sys

import raisefunction.tests


def main() -> int:
    return int(1 - raisefunction.tests.test().wasSuccessful())


if __name__ == "__main__":
    sys.exit(main())
