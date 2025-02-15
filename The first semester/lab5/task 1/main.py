def is_heap(arr, n):
    for i in range(1, n + 1):
        left = 2 * i
        right = 2 * i + 1

        if left <= n and arr[i - 1] > arr[left - 1]:
            return "NO"

        if right <= n and arr[i - 1] > arr[right - 1]:
            return "NO"

    return "YES"


def file_handler(input_file, output_file):
    with open(input_file, 'r') as file:
        n = int(file.readline())
        arr = list(map(int, file.readline().split()))

    result = is_heap(arr, n)

    with open(output_file, 'w') as file:
        file.write(result)


def main():
    file_handler("input.txt", "output.txt")


if __name__ == "__main__":
    main()
