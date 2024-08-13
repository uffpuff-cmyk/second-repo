import heapq

def dijkstra(graph, start):
    # Priority queue to store the nodes and their distances
    pq = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()

    while pq:
        # Get the node with the smallest distance
        current_distance, current_node = heapq.heappop(pq)

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # If a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Example usage
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

start_node = 'A'
distances = dijkstra(graph, start_node)

print("Shortest distances from node", start_node)
for node, distance in distances.items():
    print(f"Node {node}: {distance}")

