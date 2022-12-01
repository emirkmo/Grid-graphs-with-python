from typing import Protocol

from .directions import DirectionProtocol as Direction
from .grid_graph import Graph2D


class ExplorationStrategy(Protocol):
    def explore(self, state: Graph2D, directions: Direction, row: int, col: int) -> int:
        raise NotImplementedError


class DepthFirstStrategy:
    def explore(self, state: Graph2D, directions: Direction, row: int, col: int) -> int:
        """Recursive dept first graph traversal with size."""
        if not state.pass_base_conditions(row, col):
            return 0

        # We're on a node, visit it, and increment.
        state.visit(row, col)
        size = 1

        # Recurse on each direction for connected nodes.
        for direction in directions:  # type: ignore
            row_offset, col_offset = direction.offset()
            size += self.explore(state, directions, row + row_offset, col + col_offset)
        return size


class BreadthFirstStrategy:
    @staticmethod
    def get_neighbors(
        state: Graph2D, directions: Direction, row: int, col: int
    ) -> list[tuple[int, int]]:

        neighbors = []
        for direction in directions:  # type: ignore
            row_offset, col_offset = direction.offset()
            new_row, new_col = row + row_offset, col + col_offset
            if state.pass_base_conditions(new_row, new_col):
                neighbors.append((new_row, new_col))

        return neighbors

    def explore(self, state: Graph2D, directions: Direction, row: int, col: int) -> int:
        """Iterative breadth first graph traversal with size."""
        if not state.pass_base_conditions(row, col):
            return 0

        # We're on a node, visit it, and increment.
        state.visit(row, col)
        size = 1
        queue = [(row, col)]
        while len(queue) > 0:
            current_row, current_col = queue.pop(0)
            neighbors = self.get_neighbors(state, directions, current_row, current_col)
            for neighbor_row, neighbor_col in neighbors:
                queue.append((neighbor_row, neighbor_col))
                state.visit(neighbor_row, neighbor_col)
                size += 1
        return size
