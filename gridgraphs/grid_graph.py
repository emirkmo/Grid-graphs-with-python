from dataclasses import dataclass, field
from typing import Any, Optional, Protocol, Sequence

import numpy as np
from numpy.typing import ArrayLike, NDArray

from .directions import DirectionProtocol


@dataclass
class Graph2D(Protocol):
    graph: Sequence[Sequence[int]]
    rows: int
    cols: int
    positive_type: int
    visited: set[tuple[int, int]] = field(default_factory=set)
    neighbors: Optional[dict[tuple[int, int], list[tuple[int, int]]]] = field(
        default_factory=dict
    )

    def pass_base_conditions(self, row: int, col: int) -> bool:
        raise NotImplementedError

    def visit(self, row: int, col: int) -> None:
        raise NotImplementedError

    def clear_visited(self) -> None:
        raise NotImplementedError

    def get_neighbors(
        self, directions: DirectionProtocol
    ) -> dict[tuple[int, int], list[tuple[int, int]]]:
        raise NotImplementedError


@dataclass(slots=True)
class GridGraph(Graph2D):
    graph: NDArray[np.int64] = np.array([], dtype=np.int64)
    cols: int = 0
    rows: int = 0
    positive_type: int = 1

    def __post_init__(self) -> None:
        if len(self.graph) != 0:
            self.rows = len(self.graph)
            self.cols = len(self.graph[0])
        elif self.cols == 0 and self.rows == 0:
            self.graph = np.random.random_integers(
                low=0, high=1, size=(self.cols, self.rows)
            )
        else:
            raise AttributeError("One of graph or cols and rows must be given.")

    @classmethod
    def create_graph(cls, rows: int, cols: int) -> Graph2D:
        return cls(graph=np.random.random_integers(low=0, high=1, size=(rows, cols)))

    def visit(self, row: int, col: int) -> None:
        self.visited.add((row, col))

    def _in_bounds(self, row: int, col: int) -> bool:
        return 0 <= row < self.rows and 0 <= col < self.cols

    def _is_positive_type(self, row: int, col: int) -> bool:
        return self.graph[row][col] == self.positive_type

    def _not_visited(self, row: int, col: int) -> bool:
        return (row, col) not in self.visited

    def pass_base_conditions(self, row: int, col: int) -> bool:
        if not self._in_bounds(row, col):
            return False
        return self._is_positive_type(row, col) and self._not_visited(row, col)

    def clear_visited(self) -> None:
        self.visited.clear()

    def get_neighbors(
        self, directions: DirectionProtocol
    ) -> dict[tuple[int, int], list[tuple[int, int]]]:
        """Create a dictionary of nodes with their neighbors."""
        neighbors = {}
        for row in range(self.rows):
            for col in range(self.cols):
                neighbors[(row, col)] = []
                for direction in directions:  # type: ignore
                    row_offset, col_offset = direction.offset()
                    new_row, new_col = row + row_offset, col + col_offset
                    if self.pass_base_conditions(new_row, new_col):
                        neighbors[(row, col)].append((new_row, new_col))
        return neighbors
