def merge(arr, temp, left, mid, right, log):
    i, j, k = left, mid + 1, left
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1
    for i in range(left, right + 1):
        arr[i] = temp[i]
    log.append(f"{left + 1} {right + 1} {arr[left]} {arr[right]}")


def merge_sort(arr, temp, left, right, log):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, temp, left, mid, log)
        merge_sort(arr, temp, mid + 1, right, log)
        merge(arr, temp, left, mid, right, log)


def main():
    with open("input.txt", "r") as f:
        n = int(f.readline().strip())
        arr = list(map(int, f.readline().strip().split()))

    temp = arr[:]
    log = []
    merge_sort(arr, temp, 0, n - 1, log)

    with open("output.txt", "w") as f:
        f.write("\n".join(log) + "\n")
        f.write(" ".join(map(str, arr)) + "\n")

    with open("output.txt", "r") as f:
        print(f.read())


if __name__ == "__main__":
    main()
