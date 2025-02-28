def strong_connect(v, graph, visited, stack):
    visited[v] = True
    for nei in graph[v]:
        if not visited[nei]:
            strong_connect(nei, graph, visited, stack)
    stack.append(v)


def count_scc(n, graph, graph_rev):
    visited = [False] * (n + 1)
    order = []

    for i in range(1, n + 1):
        if not visited[i]:
            strong_connect(i, graph, visited, order)

    visited = [False] * (n + 1)
    count = 0

    for v in reversed(order):
        if not visited[v]:
            strong_connect(v, graph_rev, visited, [])
            count += 1

    return count


def file_handler(input_file, output_file):
    with open(input_file, 'r') as f:
        n, m = map(int, f.readline().split())
        graph = [[] for _ in range(n + 1)]
        graph_rev = [[] for _ in range(n + 1)]

        for _ in range(m):
            u, v = map(int, f.readline().split())
            graph[u].append(v)
            graph_rev[v].append(u)

    result = count_scc(n, graph, graph_rev)

    with open(output_file, 'w') as f:
        f.write(str(result) + '\n')


def main():
    file_handler("input.txt", "output.txt")


if __name__ == "__main__":
    main()
