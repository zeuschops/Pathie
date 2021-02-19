from GraphViewer import GraphViewer
from GridWithWeights import GridWithWeights
from Queue import Queue
from PriorityQueue import PriorityQueue

class AStarImplementation:
    def __init__(self, width=13, height=16):
        self.grid = GridWithWeights(width, height)
        self.gv = GraphViewer()
        self.walls = []

    def herusitic(self, a, b):
        (x1, y1) = a
        (x2, y2) = b
        return abs(x1 - x2) + abs(y1 - y2)

    def a_star_search(self, graph, start, goal):
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0
        while not frontier.empty():
            current = frontier.get()
            if current == goal:
                break
            for next in graph.neighbors(current):
                new_cost = cost_so_far[current] + graph.cost(current, next)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + self.herusitic(goal, next)
                    frontier.put(next, priority)
                    came_from[next] = current
        return came_from, cost_so_far

    def reconstruct_path(self, came_from, start, goal):
        if goal not in list(came_from):
            raise Exception("Unable to travel to location %s, please expand the grid or choose a new location within the grid boundary." % str(goal))
        current = goal
        path = []
        while current != start:
            path.append(current)
            current = came_from[current]
        path.append(start)
        path.reverse()
        return path
