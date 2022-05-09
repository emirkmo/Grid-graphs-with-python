from enum import Enum, auto
from typing import Protocol


class Offsets(Enum):
    up = 1, 0
    down = -1, 0
    left = 0, -1
    right = 0, 1
    up_left = 1, -1
    up_right = 1, 1
    down_left = -1, -1
    down_right = -1, 1


class DirectionProtocol(Protocol):
    def offset(self: Enum) -> tuple[int, int]:
        return Offsets[self.name].value

    def __iter__(self) -> iter:
        ...


class Direction(Enum):
    def offset(self) -> tuple[int, int]:
        return Offsets[self.name].value


class Cardinal(Direction):
    up = auto()
    down = auto()
    left = auto()
    right = auto()


class Diagonal(Direction):
    up = auto()
    down = auto()
    left = auto()
    right = auto()
    up_left = auto()
    up_right = auto()
    down_left = auto()
    down_right = auto()
