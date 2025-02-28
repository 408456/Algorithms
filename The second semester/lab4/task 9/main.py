def find_repeats(s):
    n = len(s)
    dp = [[""] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = s[i]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = s[i:j + 1]

            for k in range(i, j):
                if len(dp[i][j]) > len(dp[i][k]) + 1 + len(dp[k + 1][j]):
                    dp[i][j] = dp[i][k] + "+" + dp[k + 1][j]

            for k in range(1, length):
                if length % k == 0 and s[i:i + k] * (length // k) == s[i:j + 1]:
                    compressed = dp[i][i + k - 1] + "*" + str(length // k)
                    if len(compressed) < len(dp[i][j]):
                        dp[i][j] = compressed

    return dp[0][n - 1]


def file_handler(input_file, output_file):
    with open(input_file, "r") as file:
        s = file.readline().strip()

    result = find_repeats(s)

    with open(output_file, "w") as file:
        file.write(result + "\n")


def main():
    file_handler("input.txt", "output.txt")


if __name__ == "__main__":
    main()


