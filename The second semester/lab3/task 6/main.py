from collections import deque


def bfs(n, graph, start, end):
    dist = [-1] * (n + 1)
    dist[start] = 0
    queue = deque([start])

    while queue:
        v = queue.popleft()

        if v == end:
            return dist[v]

        for nei in graph[v]:
            if dist[nei] == -1:
                dist[nei] = dist[v] + 1
                queue.append(nei)

    return -1


def file_handler(input_file, output_file):
    with open(input_file, 'r') as f:
        n, m = map(int, f.readline().split())
        graph = [[] for _ in range(n + 1)]

        for _ in range(m):
            u, v = map(int, f.readline().split())
            graph[u].append(v)
            graph[v].append(u)

        start, end = map(int, f.readline().split())

    result = bfs(n, graph, start, end)

    with open(output_file, 'w') as f:
        f.write(str(result) + '\n')


def main():
    file_handler("input.txt", "output.txt")


if __name__ == "__main__":
    main()
