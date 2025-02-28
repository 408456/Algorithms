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

    def insert(self, node, key):
        if not node:
            return AVLNode(key)
        if key < node.key:
            node.left = self.insert(node.left, key)
        elif key > node.key:
            node.right = self.insert(node.right, key)
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        return self.balance(node)

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
            min_larger_node = self.get_min(node.right)
            node.key = min_larger_node.key
            node.right = self.delete(node.right, min_larger_node.key)
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        return self.balance(node)

    def exists(self, node, key):
        if not node:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self.exists(node.left, key)
        else:
            return self.exists(node.right, key)

    def get_min(self, node):
        while node.left:
            node = node.left
        return node

    def get_max(self, node):
        while node.right:
            node = node.right
        return node

    def next(self, node, key):
        successor = None
        while node:
            if key < node.key:
                successor = node
                node = node.left
            else:
                node = node.right
        return successor.key if successor else 'none'

    def prev(self, node, key):
        predecessor = None
        while node:
            if key > node.key:
                predecessor = node
                node = node.right
            else:
                node = node.left
        return predecessor.key if predecessor else 'none'

    def process(self, command, x):
        if command == 'insert':
            self.root = self.insert(self.root, x)
        elif command == 'delete':
            self.root = self.delete(self.root, x)
        elif command == 'exists':
            return 'true' if self.exists(self.root, x) else 'false'
        elif command == 'next':
            return str(self.next(self.root, x))
        elif command == 'prev':
            return str(self.prev(self.root, x))
        return None


def file_handler(input_file, output_file):
    tree = AVLTree()
    results = []

    with open(input_file, 'r') as f:
        for line in f:
            parts = line.split()
            command, x = parts[0], int(parts[1])
            result = tree.process(command, x)
            if result is not None:
                results.append(result)

    with open(output_file, 'w') as f:
        f.write('\n'.join(results) + '\n')


def main():
    file_handler("input.txt", "output.txt")


if __name__ == "__main__":
    main()
