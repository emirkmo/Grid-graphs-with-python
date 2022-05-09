from grid_graph import GridGraph
from directions import Diagonal, Cardinal
from strategies import DepthFirstStrategy, BreadthFirstStrategy
from islands import get_island_stats


def main() -> None:
    graph = GridGraph.create_graph(rows=50, cols=50)
    for direction in [Diagonal, Cardinal]:
        for strategy in [DepthFirstStrategy, BreadthFirstStrategy]:
            print(f"{strategy.__name__} {direction.__name__}")
            stats = get_island_stats(graph, strategy(), direction)
            print(stats)
            graph.clear_visited()


if __name__ == '__main__':
    main()
