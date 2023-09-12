import sys
import itertools

# Define a constant representing an infinite distance (used as placeholder for unconnected nodes)
NO_PATH = sys.maxsize

# Create a graph represented as an adjacency matrix
graph = [
    [0,       7,       NO_PATH, 8],
    [NO_PATH, 0,       5,       NO_PATH],
    [NO_PATH, NO_PATH, 0,       2],
    [NO_PATH, NO_PATH, NO_PATH, 0]
]

# Get the number of nodes in the graph (assuming it's a square matrix)
MAX_LENGTH = len(graph[0])

# Define the Floyd-Warshall algorithm to find all shortest paths


def floyd(distance):
    # Iterate through all possible intermediate nodes, start nodes, and end nodes
    for intermediate, start_node, end_node in itertools.product(range(MAX_LENGTH), range(MAX_LENGTH), range(MAX_LENGTH)):
        if start_node == end_node:
            # Distance from a node to itself is always 0
            distance[start_node][end_node] = 0
            continue

        # Update the distance if a shorter path through the intermediate node is found
        distance[start_node][end_node] = min(
            distance[start_node][end_node], distance[start_node][intermediate] + distance[intermediate][end_node])

    return distance


# Print the result of the Floyd-Warshall algorithm
print(floyd(graph))
