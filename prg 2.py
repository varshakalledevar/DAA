from itertools import permutations

def calculate_distance(route, distances):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distances[route[i]][route[i + 1]]
    total_distance += distances[route[-1]][route[0]]
    return total_distance

def brute_force_tsp(distances, start):
    n = len(distances)
    cities = [i for i in range(n) if i != start]
    min_distance = float('inf')
    shortest_route = None
    print("\nAll Possible Routes and Their Distances:\n")
    for perm in permutations(cities):
        current_route = [start] + list(perm) + [start]
        current_distance = calculate_distance(current_route, distances)
        print(f"Route {current_route} → Distance = {current_distance}")
        if current_distance < min_distance:
            min_distance = current_distance
            shortest_route = current_route
    return shortest_route, min_distance
n = int(input("Enter number of cities: "))
print("Enter the distance matrix row by row (use spaces between values):")
distances = []
for i in range(n):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    distances.append(row)
start = int(input(f"Enter the starting node (0 to {n-1}): "))
route, total_distance = brute_force_tsp(distances, start)
print("\nShortest Route:", route)
print("Minimum Distance:", total_distance)

