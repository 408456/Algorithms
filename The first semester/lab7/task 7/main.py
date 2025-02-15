def match(pattern, string):
    m = len(pattern)
    n = len(string)

    dp = [[False] * (n + 1) for _ in range(m + 1)]

    dp[0][0] = True

    for i in range(1, m + 1):
        if pattern[i - 1] == '*':
            dp[i][0] = dp[i - 1][0]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if pattern[i - 1] == string[j - 1] or pattern[i - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif pattern[i - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

    return "YES" if dp[m][n] else "NO"


def file_handler():
    with open('input.txt', 'r') as f:
        pattern = f.readline().strip()
        string = f.readline().strip()

    result = match(pattern, string)

    with open('output.txt', 'w') as f:
        f.write(result)


def main():
    file_handler()


if __name__ == "__main__":
    main()
