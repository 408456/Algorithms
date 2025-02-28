from collections import deque


def bfs(matrix, start_x, start_y, qx, qy, n, m, L):
    visited = [[False] * m for _ in range(n)]
    queue = deque([(start_x, start_y, 0)])

    while queue:
        x, y, dist = queue.popleft()

        if x == qx and y == qy and dist <= L:
            return True

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and matrix[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))

    return False


def count_pendants(matrix, positions, qx, qy, n, m, L):
    total = 0

    for x, y, p in positions:
        if bfs(matrix, x - 1, y - 1, qx - 1, qy - 1, n, m, L):
            total += p

    return total


def file_handler(input_file, output_file):
    with open(input_file, 'r') as f:
        n, m = map(int, f.readline().split())
        matrix = [list(map(int, list(f.readline().strip()))) for _ in range(n)]

        qx, qy, L = map(int, f.readline().split())
        positions = [tuple(map(int, f.readline().split())) for _ in range(4)]

    result = count_pendants(matrix, positions, qx, qy, n, m, L)

    with open(output_file, 'w') as f:
        f.write(str(result) + '\n')


def main():
    file_handler("input.txt", "output.txt")


if __name__ == "__main__":
    main()
