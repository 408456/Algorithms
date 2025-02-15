def operation(command, value, data_set):
    if command == 'A':
        data_set.add(value)
    elif command == 'D':
        data_set.remove(value)
    elif command == '?':
        return 'Y' if value in data_set else 'N'
    print(data_set)


def file_handler(input_file, output_file):
    data_set = set()
    results = []

    with open(input_file, 'r') as f:
        lines = f.readlines()

    for line in lines[1:]:
        parts = line.split()
        command, value = parts[0], int(parts[1])
        result = operation(command, value, data_set)
        if result is not None:
            results.append(result)

    with open(output_file, 'w') as f:
        f.write('\n'.join(results) + '\n')


def main():
    file_handler('input.txt', 'output.txt')


if __name__ == "__main__":
    main()
