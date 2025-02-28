def is_bst(node, low, high, tree):
    if node == -1:
        return True
    key, left, right = tree[node]

    if key <= low or key >= high:
        return False

    return is_bst(left, low, key, tree) and is_bst(right, key, high, tree)


def check_bst(n, tree):
    if n == 0:
        return "CORRECT"

    return "CORRECT" if is_bst(0, -float('inf'), float('inf'), tree) else "INCORRECT"


def file_handler(input_file, output_file):
    with open(input_file, 'r') as f:
        n = int(f.readline())
        tree = []

        for _ in range(n):
            k, l, r = map(int, f.readline().split())
            tree.append((k, l, r))

    result = check_bst(n, tree)

    with open(output_file, 'w') as f:
        f.write(result + '\n')


def main():
    file_handler("input.txt", "output.txt")


if __name__ == "__main__":
    main()
