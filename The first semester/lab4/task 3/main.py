def is_valid_sequence(sequence):
    stack = []
    bracket_pairs = {')': '(', ']': '['}

    for char in sequence:
        if char in bracket_pairs.values():
            stack.append(char)
        elif char in bracket_pairs:
            if not stack or stack.pop() != bracket_pairs[char]:
                return "NO"

    return "YES" if not stack else "NO"


def file_handler(input_file, output_file):
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        lines = infile.readlines()
        if not lines:
            return

        n = int(lines[0].strip())
        sequences = lines[1:n + 1]
        results = [is_valid_sequence(line.strip()) for line in sequences]
        outfile.write("\n".join(results) + "\n")


def main():
    file_handler("input.txt", "output.txt")


if __name__ == "__main__":
    main()
