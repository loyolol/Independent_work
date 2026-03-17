# Задание №1. Поиск кратчайшего пути (жадный выбор)

def find_path(matrix, start):
    n = len(matrix)
    visited = [False] * n
    path = [start]
    visited[start] = True
    total_distance = 0
    current = start
    
    for _ in range(n - 1):
        nearest = -1
        min_dist = float('inf')
        
        for i in range(n):
            if not visited[i] and matrix[current][i] < min_dist and matrix[current][i] > 0:
                min_dist = matrix[current][i]
                nearest = i
        
        if nearest != -1:
            path.append(nearest)
            visited[nearest] = True
            total_distance += min_dist
            current = nearest
    
    if len(path) == n:
        total_distance += matrix[path[-1]][start]
        path.append(start)
    
    return path, total_distance

cities = ['A', 'B', 'C', 'D']
matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

start_index = 0
path_indices, total = find_path(matrix, start_index)
path_names = [cities[i] for i in path_indices]

print("Кратчайший путь из чтобы посетить все точки:")
print(" → ".join(path_names))
print(f"Займёт этот путь: {total}")