def nearest_neighbor(graph):
    n = len(graph)
    tour = [0]  # Start from city 0
    visited = [False] * n
    visited[0] = True
    
    for _ in range(n - 1):
        current_city = tour[-1]
        min_distance = float('inf')
        nearest_city = None
        
        for next_city in range(n):
            if not visited[next_city] and graph[current_city][next_city] < min_distance:
                min_distance = graph[current_city][next_city]
                nearest_city = next_city
        
        tour.append(nearest_city)
        visited[nearest_city] = True
    
    tour.append(0)  # Return to the starting city
    return tour

def print_path(path, graph):
    total_cost = 0
    for i in range(len(path) - 1):
        total_cost += graph[path[i]][path[i+1]]
        print(f"Move from city {path[i]} to city {path[i+1]}, cost: {graph[path[i]][path[i+1]]}")
    print(f"Total cost of the path: {total_cost}")

if __name__ == "__main__":
    print("Enter the number of cities:")
    n = int(input())
    
    print("Enter the costs for the edges of the graph (separated by spaces):")
    graph = [list(map(int, input().split())) for _ in range(n)]
    
    min_path = nearest_neighbor(graph)
    print("Shortest path:")
    print_path(min_path, graph)
