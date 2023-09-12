import sys
import itertools

# Define a constant representing an infinite distance (used as a placeholder for unconnected nodes)
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

# Define a recursive function to find the shortest path between two nodes


def shortest_path(start, end, intermediate, distance):

    # Base case: If the intermediate value is less than 0, return the direct distance
    if intermediate < 0:
        return distance[start][end]

    # Recursive case: Find the minimum distance by considering or bypassing the intermediate node
    return min(
        shortest_path(start, end, intermediate - 1, distance),
        shortest_path(start, intermediate, intermediate - 1, distance) +
        shortest_path(intermediate, end, intermediate - 1, distance)
    )

# Define the Floyd-Warshall algorithm to find all shortest paths


def floyd(distance):

    for start_node, end_node in itertools.product(range(MAX_LENGTH), range(MAX_LENGTH)):

        if start_node == end_node:
            # Distance from a node to itself is always 0
            distance[start_node][end_node] = 0
            continue

        # Use the shortest_path function to find the shortest path between start_node and end_node
        distance[start_node][end_node] = shortest_path(
            start_node, end_node, MAX_LENGTH - 1, distance)

    return distance


if __name__ == '__main__':
    # Print the result of the Floyd-Warshall algorithm
    print(floyd(graph))
