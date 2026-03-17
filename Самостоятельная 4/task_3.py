# Задание №3. Поиск количества путей

graph = {
    'А': ['Б', 'В', 'Г', 'Д'],
    'Б': ['А', 'Е'],
    'В': ['А', 'Б', 'Г', 'З', 'Е'],
    'Г': ['А', 'В', 'Д', 'З'],
    'Д': ['А', 'Г', 'З'],
    'Е': ['Б', 'В', 'Ж', 'И'],
    'Ж': ['Е', 'В', 'З', 'И'],
    'З': ['В', 'Г', 'Д', 'Ж', 'И'],
    'И': ['Е', 'Ж', 'З']
}

def count_paths_with_city(current, end, visited, target_city, passed_target):
    if current == end and passed_target:
        return 1
    
    count = 0
    for neighbor in graph[current]:
        if neighbor not in visited:
            new_passed = passed_target or (neighbor == target_city)
            count += count_paths_with_city(neighbor, end, visited + [current], target_city, new_passed)
    
    return count

start = 'А'
end = 'И'
target = 'В'

total_paths = count_paths_with_city(start, end, [], target, False)
print(f"Всего путей: {total_paths}")