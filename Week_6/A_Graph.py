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
        # Filter nonsense no longer necessary because of edge list
        self.adjacencies.append((other, weight))
    
    def __str__(self):
        str_rep = "Node: " + str(self.data)
        return str_rep

class Graph:
    # Initializing an empty graph
    def __init__(self):
        self.verticies = set()
        self.edges = set() # Adding a set to track edges for MST

    # Assumes that u and v are already Vertex objects
    def add_edge(self, u, v, weight):
        #--Updating to add edge list for MST implementation--
        in_edges = False
        for edge in self.edges:
            # This kind of renders my lambda useless...
            if ((edge[0] == u) and (edge[1] == v)) or ((edge[0] == v) and (edge[1] == u)):
                in_edges = True
        if not in_edges:
            self.edges.add((v, u, weight))

            #--Regular part f adding an edge to an undirected graph--
            if u not in self.verticies:
                self.verticies.add(u)
            if v not in self.verticies:
                self.verticies.add(v)
            u.add_adjacency(v, weight)
            v.add_adjacency(u, weight)

    def display(self):
        for vert in self.verticies:
            print(str(vert))
            print("Adjacencies: ")
            for ad in vert.adjacencies:
                print(str(ad[0]), "with weight", str(ad[1]))

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

    # Creates a minimum spanning tree using (kind of) kurskal's algorithm
    def MST(self):
        # Sorting the edges by weight
        sorted_edges = sorted(self.edges, key=lambda tup: tup[2])
        # Marking nodes as univisted so cycles can't appear later on
        nodes = {e:0 for e in self.verticies}
        mst = []

        for edge in range(len(sorted_edges)):
            # Isolate the nodes
            u = sorted_edges[edge][0]
            v = sorted_edges[edge][1]
            edge_u, edge_v = None, None
            # Search sorted_edges for a short edge connected to these edges
            for adj in range(edge, len(sorted_edges)):
                if sorted_edges[adj][0] == u or sorted_edges[edge][1] == u:
                    edge_u = (sorted_edges[adj] if sorted_edges[adj][0] == u else sorted_edges[edge])
                elif sorted_edges[adj][0] == v or sorted_edges[edge][1] == v:
                    edge_v = (sorted_edges[adj] if sorted_edges[adj][0] == v else sorted_edges[edge])
                # Break the loop the moment a short connection is found for both
                if edge_u and edge_v:
                    break
            
            # If the edges are not the same  
            if edge_v != edge_u:
                if nodes[u] <= 1 and edge_u:
                    mst.append(edge_u)
                    nodes[u] = nodes[u] + 1
                if nodes[v] <= 1 and edge_v:
                    mst.append(edge_v)
                    nodes[v] = nodes[v] + 1
        return mst


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

    graph.display()

    # Running the algorithms!
    distances = graph.dijkstra(a)
    for v in distances:
        print(f"The shortest distance from Node A to {v} is {distances[v]}")

    mst = graph.MST()
    print("The minimum spanning tree for this graph is:")
    for v in mst:
        print(str(v[0]), str(v[1]), f"Weight: {v[2]}")


# Complexity for the MST implementation is currently O(E^2) because I do not check for
# visitation in the inner loop; if I check for visited nodes inside the inner loop,
# it will become O(ElogE), especially if I break early.