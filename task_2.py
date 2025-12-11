from collections import deque

graph = {
    'Київ': ['Житомир', 'Вінниця', 'Черкаси', 'Полтава', 'Чернігів'],
    'Житомир': ['Київ', 'Вінниця'],
    'Вінниця': ['Житомир', 'Київ', 'Черкаси'],
    'Черкаси': ['Вінниця', 'Київ', 'Полтава'],
    'Полтава': ['Черкаси', 'Київ', 'Чернігів'],
    'Чернігів': ['Полтава', 'Київ']
}


# Алгоритм DFS рекурсивний
def dfs_recursive(graph, vertex, visited=None, step_counter=None):
    if visited is None:
        visited = set()
    if step_counter is None:
        step_counter = [0]  # використовуємо список для передачі за посиланням
    
    step_counter[0] += 1  # лічильник кроків
    visited.add(vertex)
    print(vertex, end=' ')  # відвідуємо вершину
    
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, step_counter)
    
    return step_counter[0]


# Алгоритм DFS ітеративний:
def dfs_iterative(graph, start_vertex):
    visited = set()
    # Використовуємо стек для зберігання вершин
    stack = [start_vertex]
    step_counter = 0
    
    while stack:
        # Вилучаємо вершину зі стеку
        vertex = stack.pop()
        step_counter += 1  # Лічильник кроків
        
        if vertex not in visited:
            print(vertex, end=' ')
            # Відвідуємо вершину
            visited.add(vertex)
            # Додаємо сусідні вершини до стеку
            stack.extend(reversed(graph[vertex]))
    
    return step_counter


# Алгоритм BFS рекурсивний:
def bfs_recursive(graph, queue, visited=None, step_counter=None):
    # Перевіряємо, чи існує множина відвіданих вершин, якщо ні, то ініціалізуємо нову
    if visited is None:
        visited = set()
    if step_counter is None:
        step_counter = [0]  # Використовуємо список для передачі за посиланням
    
    # Якщо черга порожня, завершуємо рекурсію
    if not queue:
        return step_counter[0]
    
    # Вилучаємо вершину з початку черги
    vertex = queue.popleft()
    step_counter[0] += 1  # Лічильник кроків
    
    # Перевіряємо, чи відвідували раніше дану вершину
    if vertex not in visited:
        # Якщо не відвідували, друкуємо вершину
        print(vertex, end=" ")
        # Додаємо вершину до множини відвіданих вершин.
        visited.add(vertex)
        # Додаємо невідвіданих сусідів даної вершини в кінець черги.
        queue.extend(set(graph[vertex]) - visited)
    
    # Рекурсивний виклик функції з тією ж чергою та множиною відвіданих вершин
    bfs_recursive(graph, queue, visited, step_counter)
    return step_counter[0]


# Алгоритм BFS ітеративний:
def bfs_iterative(graph, start):
    # Ініціалізація порожньої множини для зберігання відвіданих вершин
    visited = set()
    # Ініціалізація черги з початковою вершиною
    queue = deque([start])
    step_counter = 0

    while queue:  # Поки черга не порожня, продовжуємо обхід
        # Вилучаємо першу вершину з черги
        vertex = queue.popleft()
        step_counter += 1  # Лічильник кроків
        
        # Перевіряємо, чи була вершина відвідана раніше
        if vertex not in visited:
            # Якщо не була відвідана, друкуємо її
            print(vertex, end=" ")
            # Додаємо вершину до множини відвіданих вершин
            visited.add(vertex)
            # Додаємо всіх невідвіданих сусідів вершини до кінця черги
            # Операція різниці множин вилучає вже відвідані вершини зі списку сусідів
            queue.extend(set(graph[vertex]) - visited)
    
    # Повертаємо кількість кроків
    return step_counter


print("Алгоритм DFS рекурсивний: ", end="")
dfs_steps = dfs_recursive(graph, 'Київ')
print(f"\nКількість кроків: {dfs_steps}")

print("\nАлгоритм DFS ітеративний: ", end="")
dfs_steps = dfs_iterative(graph, 'Київ')
print(f"\nКількість кроків: {dfs_steps}")

print("\nАлгоритм BFS рекурсивний: ", end="")
bfs_steps = bfs_recursive(graph, deque(["Київ"]))
print(f"\nКількість кроків: {bfs_steps}")

print("\nАлгоритм BFS ітеративний: ", end="")
bfs_steps = bfs_iterative(graph, 'Київ')
print(f"\nКількість кроків: {bfs_steps}")