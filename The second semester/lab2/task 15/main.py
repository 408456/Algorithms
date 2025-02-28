class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        return y

    def balance(self, node):
        balance_factor = self.get_balance(node)
        if balance_factor > 1:
            if self.get_balance(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance_factor < -1:
            if self.get_balance(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node

    def find_max(self, node):
        while node.right:
            node = node.right
        return node

    def delete(self, node, key):
        if not node:
            return node

        if key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            temp = self.find_max(node.left)
            node.key = temp.key
            node.left = self.delete(node.left, temp.key)

        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        return self.balance(node)

    def build_tree(self, nodes):
        if not nodes:
            return None

        node_dict = {i + 1: AVLNode(k) for i, (k, _, _) in enumerate(nodes)}
        for i, (k, l, r) in enumerate(nodes):
            if l:
                node_dict[i + 1].left = node_dict[l]
            if r:
                node_dict[i + 1].right = node_dict[r]

        self.root = node_dict[1] if nodes else None

    def serialize_tree(self):
        if not self.root:
            return "0"

        result, queue, index_map = [], [(self.root, 1)], {}
        index = 1

        while queue:
            node, idx = queue.pop(0)
            index_map[node] = idx
            left_idx = index + 1 if node.left else 0
            right_idx = index + 2 if node.right else 0
            if node.left:
                queue.append((node.left, left_idx))
            if node.right:
                queue.append((node.right, right_idx))
            index += (1 if node.left else 0) + (1 if node.right else 0)
            result.append(f"{node.key} {left_idx} {right_idx}")

        return f"{len(result)}\n" + "\n".join(result)


def file_handler(input_file, output_file):
    with open(input_file, "r") as f:
        lines = f.readlines()

    n = int(lines[0])
    nodes = [tuple(map(int, lines[i].split())) for i in range(1, n + 1)]
    key_to_delete = int(lines[n + 1])

    tree = AVLTree()
    tree.build_tree(nodes)
    tree.root = tree.delete(tree.root, key_to_delete)

    with open(output_file, "w") as f:
        f.write(tree.serialize_tree())


def main():
    file_handler("input.txt", "output.txt")


if __name__ == "__main__":
    main()
