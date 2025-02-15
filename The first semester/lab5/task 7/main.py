def max_heapify(arr, n, i):
    maxi = i
    left = 2 * i + 1
    right = 2 * i + 2

    while True:
        if left < n and arr[left] > arr[maxi]:
            maxi = left

        if right < n and arr[right] > arr[maxi]:
            maxi = right

        if maxi != i:
            arr[i], arr[maxi] = arr[maxi], arr[i]
            i = maxi
            left = 2 * i + 1
            right = 2 * i + 2
        else:
            break


def heapsort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # корень в конец
        max_heapify(arr, i, 0)


def file_handler(input_file, output_file):
    with open(input_file, 'r') as file:
        n = int(file.readline())
        arr = list(map(int, file.readline().split()))
    heapsort(arr)
    with open(output_file, 'w') as file:
        file.write(" ".join(map(str, arr)))


def main():
    file_handler("input.txt", "output.txt")


if __name__ == "__main__":
    main()
