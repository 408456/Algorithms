def lis(arr):
    n = len(arr)
    dp = [1] * n
    prev = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j

    max_len = max(dp)
    index = dp.index(max_len)

    subsequence = []
    while index != -1:
        subsequence.append(arr[index])
        index = prev[index]

    subsequence.reverse()
    return max_len, subsequence


def file_handler(input_file, output_file):
    with open(input_file, 'r') as f:
        n = int(f.readline().strip())
        arr = list(map(int, f.readline().split()))

    max_len, subsequence = lis(arr)

    with open(output_file, 'w') as f:
        f.write(f"{max_len}\n")
        f.write(" ".join(map(str, subsequence)) + "\n")


def main():
    file_handler("input.txt", "output.txt")


if __name__ == "__main__":
    main()
