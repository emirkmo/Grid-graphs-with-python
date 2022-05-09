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
