import sys
import itertools

NO_PATH = sys.maxsize
graph = [
    [0,       7,       NO_PATH, 8       ],
    [NO_PATH, 0,       5,       NO_PATH ],
    [NO_PATH, NO_PATH, 0,       2       ],
    [NO_PATH, NO_PATH, NO_PATH, 0       ]
]
MAX_LENGTH = len(graph[0])

def shortest_path(start, end, intermediate, distance):

    # base case
    if intermediate < 0:
        return distance[start][end]
    
    return min(
        shortest_path(start, end, intermediate - 1, distance),
        shortest_path(start, intermediate , intermediate - 1, distance) + shortest_path(intermediate, end, intermediate - 1, distance)
    )
    
def floyd(distance):

    for start_node , end_node in itertools.product(range(MAX_LENGTH), range(MAX_LENGTH)):
        
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue

        distance[start_node][end_node] = shortest_path(start_node, end_node, MAX_LENGTH - 1 , distance)

    return distance
    
if __name__ == '__main__':
    print(floyd(graph))
