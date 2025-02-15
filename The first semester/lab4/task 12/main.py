class Soldier:
    def __init__(self, number):
        self.number = number
        self.left = None
        self.right = None


class Army:
    def __init__(self, n):
        self.soldiers = [Soldier(i) for i in range(1, n + 1)]
        self.soldier_positions = {i: self.soldiers[i - 1] for i in range(1, n + 1)}
        self.head = self.soldiers[0]
        self.head.left = None
        self.head.right = None

    def left(self, I, J):
        soldier_I = self.soldier_positions[I]
        soldier_J = self.soldier_positions[J]

        soldier_I.left = soldier_J.left
        soldier_I.right = soldier_J
        if soldier_J.left:
            soldier_J.left.right = soldier_I
        soldier_J.left = soldier_I

        # J -> I 1
        if soldier_J == self.head:
            self.head = soldier_I

    def right(self, I, J):
        soldier_I = self.soldier_positions[I]
        soldier_J = self.soldier_positions[J]
        soldier_I.right = soldier_J.right
        soldier_I.left = soldier_J
        if soldier_J.right:
            soldier_J.right.left = soldier_I
        soldier_J.right = soldier_I

    def leave(self, I):
        soldier_I = self.soldier_positions[I]
        if soldier_I.left:
            soldier_I.left.right = soldier_I.right
        if soldier_I.right:
            soldier_I.right.left = soldier_I.left
        if soldier_I == self.head:
            self.head = soldier_I.right

    def name(self, I):
        soldier_I = self.soldier_positions[I]
        left_neighbor = soldier_I.left.number if soldier_I.left else 0
        right_neighbor = soldier_I.right.number if soldier_I.right else 0
        return left_neighbor, right_neighbor


def file_handler(input_file, output_file):
    with open(input_file) as infile, open(output_file, 'w') as outfile:
        n, m = map(int, infile.readline().strip().split())
        army = Army(n)

        for _ in range(m):
            command = infile.readline().strip().split()

            if command[0] == "left":
                I = int(command[1])
                J = int(command[2])
                army.left(I, J)
            elif command[0] == "right":
                I = int(command[1])
                J = int(command[2])
                army.right(I, J)
            elif command[0] == "leave":
                I = int(command[1])
                army.leave(I)
            elif command[0] == "name":
                I = int(command[1])
                left, right = army.name(I)
                outfile.write(f"{left} {right}\n")


def main():
    file_handler('txt/i1.txt', 'txt/o1.txt')
    file_handler('txt/i2.txt', 'txt/o2.txt')


if __name__ == "__main__":
    main()
