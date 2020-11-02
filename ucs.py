from queue import PriorityQueue

class Graph:
    def __init__(self):
        self.edges = {}
        self.weights = {}

    def neighbors(self, node):
        return self.edges[node]

    def get_cost(self, from_node, to_node):
        return self.weights[(from_node + to_node)]



def uniform_cost_search(graph, start_node, goal):
   
    path = set()
    explored = set()

    if start_node == goal:
        return path, explored

    path.add(start_node)
    path_cost = 0
    frontier = PriorityQueue()
    frontier.put((path_cost, start_node))

    while frontier:
        cost, node = frontier.get()

        if node not in explored:
            explored.add(node)
        if node == goal:
            print("Path Available")
            print("At the cost of " + str(cost))
            return

        for neighbor in graph.neighbors(node):
            if neighbor not in explored:
                total_cost = cost + graph.get_cost(node, neighbor)
                frontier.put((total_cost, neighbor))




# Driver Function
edges = {
    'S': ['1', '3'],
    '1': ['G'],
    '2': ['1'],
    '3': ['1','G','4'],
    '4': ['2','5'],
    '5': ['2','G'],
    'G': ['4']
}
weigth = {
    'S1': 2,
    'S3': 5,
    '1G': 1,
    '21': 4,
    '31': 5,
    '34': 2,
    '3G': 6,
    '42':4,
    '45':3,
    '52':6,
    '5G':3,
    'G4':7
}

simple_graph = Graph()
simple_graph.edges = edges
simple_graph.weights = weigth

uniform_cost_search(simple_graph, 'S', 'G')