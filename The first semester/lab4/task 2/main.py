from collections import deque


def queue_operations(input_file, output_file):
    with open(input_file) as infile, open(output_file, 'w') as outfile:
        queue = deque()
        for line in infile.readlines()[1:]:
            if line[0] == '+':
                queue.append(line.split()[1])
            else:
                outfile.write(queue.popleft() + '\n')
    print(queue)


def main():
    queue_operations('input.txt', 'output.txt')


if __name__ == "__main__":
    main()
