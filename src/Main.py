from Graph import Graph
from Queue import Queue
from SquareGrid import SquareGrid
from PriorityQueue import PriorityQueue
from AStarImplementation import AStarImplementation
from GridWithWeights import GridWithWeights
from GraphViewer import GraphViewer

gv = GraphViewer()

astar_impl = AStarImplementation()
diagram4 = GridWithWeights(10, 10)
diagram4.walls = [(1, 7), (1, 8), (2, 7), (2, 8), (3, 7), (3, 8)] #These can be easily changed
diagram4.weights = {loc: 2 for loc in [(3, 4), (3, 5), (4, 1), (4, 2),
                                       (4, 3), (4, 4), (4, 5), (4, 6),
                                       (4, 7), (4, 8), (5, 1), (5, 2),
                                       (5, 3), (5, 4), (5, 5), (5, 6),
                                       (5, 7), (5, 8), (6, 2), (6, 3),
                                       (6, 4), (6, 5), (6, 6), (6, 7),
                                       (7, 3), (7, 4), (7, 5)]} #Weights can also be easily changed :-)

def debuggingGrids(diagram4, width, point_to, number, start, goal):
    gv.draw_grid(diagram4, width=3, point_to=came_from, start=start, goal=goal)
    print()
    gv.draw_grid(diagram4, width=3, number=cost_so_far, start=start, goal=goal)
    print()

#Define some routing information - as well as print out the actual path from running the a_star_search method in AStarImplementation()
start, goal = (1,4), (9, 9)
came_from, cost_so_far = astar_impl.a_star_search(diagram4, start, goal)
#debuggingGrids(diagram4, 3, came_from, cost_so_far, start, goal)
gv.draw_grid(diagram4, width=3, path=astar_impl.reconstruct_path(came_from, start=start, goal=goal))
print()
