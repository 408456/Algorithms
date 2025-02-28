# вывести строку максимальной длины
def delete_caps(s):
    stack = []
    result = []
    for char in s:
        if char in '({[':
            stack.append((char, len(result)))
            result.append(None)
        elif char in ')}]':
            if stack and ((stack[-1][0] == '(' and char == ')') or
                          (stack[-1][0] == '[' and char == ']') or
                          (stack[-1][0] == '{' and char == '}')):
                last_open, index = stack.pop()
                result[index] = last_open
                result.append(char)
    return ''.join(c for c in result if c is not None)


def file_handler(input_file, output_file):
    with open(input_file, "r") as f:
        s = f.readline().strip()

    result = delete_caps(s)

    with open(output_file, "w") as f:
        f.write(result + "\n")


def main():
    file_handler("input.txt", "output.txt")


if __name__ == "__main__":
    main()
