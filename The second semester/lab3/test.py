graph_matrix = [
    [0, 1, 0, 0],
    [1, 0, 1, 1],
    [0, 1, 0, 1],
    [0, 1, 1, 0]
]

graph_list = {
    0: [1],
    1: [0, 2, 3],
    2: [1, 3],
    3: [1, 2]
}


# обход в глубину

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


graph_list = {
    0: [1],
    1: [0, 2, 3],
    2: [1, 3],
    3: [1, 2]
}

dfs(graph_list, 0)


# достижимость
def is_reachable(graph, start, end):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex == end:
            return True
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex])
    return False


print(is_reachable(graph_list, 0, 3))


# компоненты связности
def connected_components(graph):
    visited = set()
    components = []

    for vertex in graph:
        if vertex not in visited:
            component = []
            dfs_collect(graph, vertex, visited, component)
            components.append(component)

    return components


def dfs_collect(graph, vertex, visited, component):
    visited.add(vertex)
    component.append(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_collect(graph, neighbor, visited, component)


print(connected_components(graph_list))

# метки времени
time = 0


def dfs_with_time(graph, vertex, visited, entry, exit):
    global time
    visited.add(vertex)
    time += 1
    entry[vertex] = time
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_with_time(graph, neighbor, visited, entry, exit)
    time += 1
    exit[vertex] = time


entry_time = {}
exit_time = {}
visited = set()
dfs_with_time(graph_list, 0, visited, entry_time, exit_time)

print("Entry:", entry_time)
print("Exit:", exit_time)


# топологическая сортировка
def topological_sort(graph):
    visited = set()
    stack = []

    def dfs(vertex):
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(vertex)

    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)

    return stack[::-1]


oriented_graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
}

print("Topological sort:", topological_sort(oriented_graph))


# сильно связные компоненты
def tarjans_scc(graph):
    index = 0
    stack = []
    indices = {}
    low_link = {}
    result = []

    def strongconnect(vertex):
        nonlocal index
        indices[vertex] = index
        low_link[vertex] = index
        index += 1
        stack.append(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in indices:
                strongconnect(neighbor)
                low_link[vertex] = min(low_link[vertex], low_link[neighbor])
            elif neighbor in stack:
                low_link[vertex] = min(low_link[vertex], indices[neighbor])

        if low_link[vertex] == indices[vertex]:
            scc = []
            while True:
                w = stack.pop()
                scc.append(w)
                if w == vertex:
                    break
            result.append(scc)

    for vertex in graph:
        if vertex not in indices:
            strongconnect(vertex)

    return result


oriented_graph_scc = {
    0: [1],
    1: [2],
    2: [0, 3],
    3: [4],
    4: [5],
    5: [3]
}

print(tarjans_scc(oriented_graph_scc))
