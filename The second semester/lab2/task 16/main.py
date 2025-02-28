class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
        self.size = 1  # Размер поддерева


class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        return node.height if node else 0

    def get_size(self, node):
        return node.size if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        y.size = self.get_size(y.left) + self.get_size(y.right) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        x.size = self.get_size(x.left) + self.get_size(x.right) + 1
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        x.size = self.get_size(x.left) + self.get_size(x.right) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        y.size = self.get_size(y.left) + self.get_size(y.right) + 1
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
        node.size = self.get_size(node.left) + self.get_size(node.right) + 1
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
        node.size = self.get_size(node.left) + self.get_size(node.right) + 1
        return self.balance(node)

    def get_min(self, node):
        while node.left:
            node = node.left
        return node

    def get_max(self, node):
        while node.right:
            node = node.right
        return node

    def find_kth_max(self, node, k):
        if not node:
            return None
        right_size = self.get_size(node.right)
        if right_size + 1 == k:
            return node.key
        elif right_size + 1 > k:
            return self.find_kth_max(node.right, k)
        else:
            return self.find_kth_max(node.left, k - right_size - 1)

    def process(self, command, x):
        if command == 'insert':
            self.root = self.insert(self.root, x)
        elif command == 'delete':
            self.root = self.delete(self.root, x)
        elif command == 'find_kth_max':
            return self.find_kth_max(self.root, x)
        return None


def file_handler(input_file, output_file):
    tree = AVLTree()
    results = []

    with open(input_file, 'r') as f:
        n = int(f.readline())
        for line in f:
            parts = line.split()
            command = int(parts[0])
            k = int(parts[1])

            if command == 1:
                tree.process('insert', k)
            elif command == 0:
                result = tree.process('find_kth_max', k)
                if result is not None:
                    results.append(str(result))
            elif command == -1:
                tree.process('delete', k)

    with open(output_file, 'w') as f:
        f.write('\n'.join(results) + '\n')


def main():
    file_handler("input.txt", "output.txt")


if __name__ == "__main__":
    main()
