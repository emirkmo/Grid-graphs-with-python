from dataclasses import dataclass, field
from typing import Optional

import numpy as np

from .directions import DirectionProtocol as Direction
from .grid_graph import Graph2D
from .strategies import ExplorationStrategy


@dataclass
class Islands:
    graph: Graph2D
    strategy: ExplorationStrategy
    valid_directions: Direction
    islands: list[int] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.graph.neighbors = self.graph.get_neighbors(self.valid_directions)
        self.get_islands()

    def get_islands(self) -> None:
        self.islands = self._get_islands(
            self.graph, self.strategy, self.valid_directions
        )

    # Given GridGraph and Strategy and valid Directions return list of islands
    @staticmethod
    def _get_islands(
        graph: Graph2D, strategy: ExplorationStrategy, directions: Direction
    ) -> list[int]:
        return [
            size
            for row in range(graph.rows)
            for col in range(graph.cols)
            if (
                size := strategy.explore(
                    state=graph, directions=directions, row=row, col=col
                )
            )
            > 0
        ]

    @property
    def island_count(self) -> int:
        return len(self.islands)

    @property
    def max_island_size(self) -> int:
        return max(self.islands)

    @property
    def min_island_size(self) -> int:
        return min(self.islands)

    @property
    def average_island_size(self) -> float:
        return sum(self.islands) / len(self.islands)

    @property
    def median_island_size(self) -> float:
        return float(np.median(self.islands))

    @property
    def mode_island_size(self) -> int:
        return max(set(self.islands), key=self.islands.count)


@dataclass
class IslandStats:
    islands: Islands = field(repr=False)
    island_count: Optional[int] = None
    max_island_size: Optional[int] = None
    min_island_size: Optional[int] = None
    average_island_size: Optional[float] = None
    median_island_size: Optional[float] = None
    mode_island_size: Optional[int] = None

    def __post_init__(self):
        if not self.islands.islands:
            self.islands.get_islands()
        self.island_count = self.islands.island_count
        self.max_island_size = self.islands.max_island_size
        self.min_island_size = self.islands.min_island_size
        self.average_island_size = self.islands.average_island_size
        self.median_island_size = self.islands.median_island_size
        self.mode_island_size = self.islands.mode_island_size


def get_island_stats(
    graph: Graph2D, strategy: ExplorationStrategy, valid_directions: Direction
) -> IslandStats:
    return IslandStats(
        islands=Islands(
            graph=graph, strategy=strategy, valid_directions=valid_directions
        )
    )
