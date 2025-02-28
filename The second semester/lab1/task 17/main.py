# 1 2 3
# 4 5 6
# 7 8! 9
# . 0! .
def my_little_pony(n):
    moves = {
        1: [8, 6], 2: [7, 9], 3: [4, 8],
        4: [3, 9], 5: [], 6: [1, 7],
        7: [2, 6], 8: [1, 3], 9: [2, 4],
        0: [4, 6]
    }

    dp = [[0] * 10 for _ in range(n + 1)]

    for i in range(1, 10):
        if i != 8 and i != 0:
            dp[1][i] = 1

    for length in range(2, n + 1):
        for digit in range(10):
            if digit != 5:
                for prev_digit in moves[digit]:
                    dp[length][digit] = (dp[length][digit] + dp[length - 1][prev_digit]) % (10 ** 9)

    return sum(dp[n])


def file_handler(input_file, output_file):
    with open(input_file, "r") as f:
        n = int(f.readline().strip())

    result = my_little_pony(n)

    with open(output_file, "w") as f:
        f.write(str(result) + "\n")


def main():
    file_handler("input.txt", "output.txt")


if __name__ == "__main__":
    main()
