class Stack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.max_stack or value >= self.max_stack[-1]:
            self.max_stack.append(value)

    def pop(self):
        if self.stack:
            value = self.stack.pop()
            if value == self.max_stack[-1]:
                self.max_stack.pop()

    def max(self):
        if self.max_stack:
            return self.max_stack[-1]
        return None

    def __repr__(self):
        return f"{self.stack}"


def file_handler(input_file, output_file):
    with open(input_file) as infile, open(output_file, 'w') as outfile:
        commands = infile.readlines()

        stack = Stack()

        for command in commands:
            parts = command.strip().split()

            if parts[0] == 'push':
                value = int(parts[1])
                stack.push(value)
            elif parts[0] == 'pop':
                stack.pop()
            elif parts[0] == 'max':
                outfile.write(str(stack.max()) + "\n")

        print(stack)  # выводим финальное состояние стека в консоль


def main():
    file_handler('input.txt', 'output.txt')


if __name__ == "__main__":
    main()
