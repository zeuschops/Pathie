from Graph import Graph
from GridWithWeights import GridWithWeights

class GraphViewer:
    def from_id_width(self, id, width):
        return (id % width, id // width)

    def draw_grid(self, graph, width=2, **style):
        for y in range(graph.height):
            for x in range(graph.width):
                print('%%-%ds' % width % self.draw_title(graph, (x, y), style, width), end="")
            print()

    def draw_title(self, graph, id, style, width):
        r = '.'
        if 'number' in style and id in style['number']: r = '%d' % style['number'][id]
        if 'point_to' in style and style['point_to'].get(id, None) is not None:
            (x1, y1) = id
            (x2, y2) = style['point_to'][id]
            if x2 == x1 + 1: r = '>'
            if x2 == x1 - 1: r = '<'
            if y2 == y1 + 1: r = 'v'
            if y2 == y1 - 1: r = '^'
        if 'start' in style and id == style['start']: r = 'A'
        if 'goal' in style and id == style['goal']: r = 'Z'
        if 'path' in style and id in style['path']: r = '@'
        if id in graph.walls: r = '#' * width
        return r
