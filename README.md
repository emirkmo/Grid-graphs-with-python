# Island graph solutions (grid graphs) with python

Connected grids can be thought of as **grid graphs**, where each grid point is a **node**
either positive (island) or negative (void/water), although the categories can be
readily inverted so in practice only one of the above is defined as the positive node. 
Connections between each grid point (node) is then an **edge**. For a given valid
connection type (say up down left right, or including diagonals) each positive 
node gets defined between 0 and maximum direction number of edges.

Common problems are:
 - count the number of islands
 - find the size of largest, smallest, average, median, mode island.
 - Use **depth-first** or **breadth-first** traversal. 

The code is fully typed and makes use of composition with Protocol classes so that valid 
directions, traversal strategies, and even 2D graph types can be readily exchanged with 
minimal refactoring.

Requires Python > 3.10.   
Only dependency is a new version of `numpy` for convenience (and typing support),
although the operations are mostly in base python data structures like `list` and `set`.

# To run

Clone and run: `python -m main.py`

# Some details and possible expansion

Grid graphs in this code can all be considered undirected but are **not** acyclical,
therefore visited nodes are marked to avoid infinite recursion. In practice, directed 2D grid
graphs are also possible to make. In that case, the neighbors should be pre-calculated as a
python dict of `{node: [list of connected nodes]}` using the provided `get_neighbors` function,
which can be done by specifying per node valid Directions, instead of a global valid_directions per graphs.

We make use of list comprehension, dataclasses, enums, protocols, and structural typing so the code may
be unfamiliar to some. Finally, the breadh-first algorithm, and the neighbor-tree generation algorithm can
be made faster by pre-computing the neighbors and having the algorithm explore the pre-computed neighbors
(edges) instead of the current version. The code for doing this is provided but unused in `grid_graph.py`
to lower coupling (as neighbors cannot be calculated without knowing valid directions, which your graph
ideally is independent of).
