'''
In this file, I'll be showing you how to implement
a basic graph with an adjacency list, and dijkstra's 
algorithm. Homework: can you convert my implementation
of dijkstra to A*?
'''
class Vertex:
    def __init__(self, data):
        self.data = data
        self.adjacencies = []

    # Only add the adjancency if it's not already there
    # Assume other is already a vertex object
    def add_adjacency(self, other, weight):
        if other not in self.adjacencies:
            self.adjacencies.append((other, weight))
    
    def __str__(self):
        str_rep = "Node: " + str(self.data)
        return str_rep

class Graph:
    # Initializing an empty graph
    def __init__(self):
        self.verticies = set()

    # Assumes that u and v are already Vertex objects
    def add_edge(self, u, v, weight):
        if u not in self.verticies:
            self.verticies.add(u)
        if v not in self.verticies:
            self.verticies.add(v)
        # Since this is an undirected graph, both edges will be added
        u.add_adjacency(v, weight)
        v.add_adjacency(u, weight)

    # Note: this implementation only gives you the distances, not
    # the paths themselves! 
    def dijkstra(self, start):
        # Set every distance to infinity to start
        distances = {v: float('infinity') for v in self.verticies}
        # And then set the start distance to 0 (the start's distance from itself is 0)
        distances[start] = 0
        # Create a list that will mimic a priority queue
        priority_queue = [(0, start)]

        # So long as our queue isn't empty
        while priority_queue:
            # Get the top of the priority queue
            current_distance, current_vertex = priority_queue.pop(0)

            # If our distance is somehow greater, just move to the next
            # item in the priority queue
            if current_distance > distances[current_vertex]:
                continue

            # Check all the adjacencies and their weights
            for neighbour, weight in current_vertex.adjacencies:
                # Updating the distance to this current node
                distance = current_distance + weight

                # Checking if the node is now reachable faster via this new
                # path.
                if distance < distances[neighbour]:
                    # Update the distance
                    distances[neighbour] = distance
                    # Prioritize this new path
                    priority_queue.insert(0, (distance, neighbour))
        # Returns all distances
        return distances

    # TODO: Implement MST

if __name__ == "__main__":
    graph = Graph()
    # Constructing some nodes
    a = Vertex('A')
    b = Vertex('B')
    c = Vertex('C')
    d = Vertex('D')
    # Connecting them in the graph
    graph.add_edge(a, b, 1)
    graph.add_edge(a, c, 4)
    graph.add_edge(b, c, 2)
    graph.add_edge(b, d, 5)
    graph.add_edge(c, d, 1)

    # Running the algorithms!
    distances = graph.dijkstra(a)
    for v in distances:
        print(f"The shortest distance from Node A to {v} is {distances[v]}")
    #print("Minimum Spanning Tree Edges:", graph.prim_mst())
