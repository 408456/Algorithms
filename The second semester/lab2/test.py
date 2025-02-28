class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class BST:
    def __init__(self):
        self.root = None

    def find(self, key, node=None):
        if node is None:
            node = self.root
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self.find(key, node.left)
        return self.find(key, node.right)

    def tree_min(self, node):
        while node.left:
            node = node.left
        return node

    def tree_max(self, node):
        while node.right:
            node = node.right
        return node

    def insert(self, key):
        new_node = Node(key)
        if self.root is None:
            self.root = new_node
            return
        parent = None
        current = self.root
        while current:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right
        new_node.parent = parent
        if key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

    def next(self, node):
        if node.right:
            return self.tree_min(node.right)
        parent = node.parent
        while parent and node == parent.right:
            node = parent
            parent = parent.parent
        return parent

    def delete(self, key):
        node = self.find(key)
        if node is None:
            return
        if node.left is None:
            self.transplant(node, node.right)
        elif node.right is None:
            self.transplant(node, node.left)
        else:
            successor = self.tree_min(node.right)
            if successor.parent != node:
                self.transplant(successor, successor.right)
                successor.right = node.right
                successor.right.parent = successor
            self.transplant(node, successor)
            successor.left = node.left
            successor.left.parent = successor

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v:
            v.parent = u.parent

    def rotate_right(self, x):
        y = x.left
        if y:
            x.left = y.right
            if y.right:
                y.right.parent = x
            y.parent = x.parent
            if x.parent is None:
                self.root = y
            elif x == x.parent.right:
                x.parent.right = y
            else:
                x.parent.left = y
            y.right = x
            x.parent = y


class AVLTree:
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

    def insert(self, root, key):
        if not root:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
        balance = self.get_balance(root)

        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if not root:
            return root

        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.rotate_right(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.rotate_left(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def pre_order(self, root):
        if root:
            print(root.key, end=" ")
            self.pre_order(root.left)
            self.pre_order(root.right)
