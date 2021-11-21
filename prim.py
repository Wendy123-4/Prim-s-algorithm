# Prim's Algorithm implementation function

# The algorithm takes weighted undirected graphs and find the
# minimum spanning tree(MST)
# The function takes 2 arguments, the graph and the node
# The graph is represented using the adjacency matrix in a 2D array
# The node is number of vertices in the graph.
# By implementing the conditions for Prim's Algorithm which are:
#    *Randomly choose a vertices to start the minimum spanning tree from.
#    *Find the minimum weight of all the edges connecting the tree to new vertices and add it to the tree.
#    *This is repeated till all nodes have been visited

# The prims function below returns the vertices with the minimum weight on their edges
# and the total weight of the Minimum Spanning Tree(MST)

def prims(graph, node):

    # Initiate variables
    # We assume the start node has the minimum weight
    # and other nodes have the highest weight
    # this because the node with the minimum weight is selected first

    # Instantiate the variable with the start node
    vertex = 0
    # We keep track of the selected node to compare with all its unvisited
    # adjacent node to find the one with the minimum weight
    # the visited_node is a boolean list that tells whether the node
    # has been visited or not
    # We initialise each node in the graph with a 0 which represents false(not visited)
    visited_node = [0]*node
    # Start with the first node by visiting it hence true
    visited_node[0] = True
    # The start node on its own has no edge so edge = 0
    edge = 0
    # This is to store the weights that make up the spanning tree
    weight_of_MST = []
    # The adjacent vertex of the initial vertex
    adjacent_vertex = 0

    # Given a MST, the maximum number of edges must be one short of the total nodes
    # This is because MST must not be connected or form any loop
    # So by the time it gets to node-1, it would have visited all vertices
    while edge < node - 1:
        # Instantiating weights of all other nodes as 1000 to differentiate
        # between start node and the rest
        minimum = 1000

        # Just like the adjacency matrix, the first node in the row
        # is compared to the all the nodes in the column
        for row in range(node):
            if visited_node[row]:
                for column in range(node):
                    if (not visited_node[column]) and graph[row][column]:
                        # the condition is it must have not been visited  and there is an edge
                        if minimum > graph[row][column]:
                            # This updates the initial minimum set to 1000 to its actual weight in the graph
                            minimum = graph[row][column]
                            # the weight gets added in the MST list
                            weight_of_MST.append(minimum)
                            # store the vertex and its qualified adjacent to print
                            vertex = row
                            adjacent_vertex = column
        if vertex == 0:
            print(str(6) + "->" + str(adjacent_vertex) + ":" + str(graph[vertex][adjacent_vertex]))
        elif adjacent_vertex == 6:
            print(str(vertex) + "->" + str(7) + ":" + str(graph[vertex][adjacent_vertex]))
        else:
            print(str(vertex) + "->" + str(adjacent_vertex) + ":" + str(graph[vertex][adjacent_vertex]))

        # adjacent vertex is updated to visited
        visited_node[adjacent_vertex] = True
        # edge increased to run the loop again
        edge += 1

    # the weight of the MST is summed to get the total weight
    total_MST = sum(weight_of_MST)
    print("\nTotal weight of Minimum Spanning Tree: " + str(total_MST) + "\n")

    return


print(prims([[0, 10, 0, 0, 0, 25, 0],
             [10, 0, 28, 0, 0, 0, 0],
             [0, 28, 0, 16, 0, 0, 14],
             [0, 0, 16, 0, 12, 0, 0],
             [0, 0, 0, 12, 0, 22, 18],
             [25, 0, 0, 0, 22, 0, 24],
             [0, 0, 14, 0, 18, 24, 0]], 7))
