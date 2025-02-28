# Сувениры. Жадный -> Динамическое
# Оценка сложности алгоритма: O(b)
def souvenirs(nums):
    sum_nums = sum(nums)
    if sum_nums % 3 != 0:
        return 0

    b = sum_nums // 3
    dp = [0] * (b + 1)
    dp[0] = 1

    for num in nums:
        for i in range(b, num - 1, -1):
            if dp[i - num]:
                dp[i] = 1

    return dp[b]


def file_handler(input_file, output_file):
    with open(input_file, "r") as f:
        n = int(f.readline().strip())
        nums = list(map(int, f.readline().split()))

    result = souvenirs(nums)

    with open(output_file, "w") as f:
        f.write(str(result) + "\n")


def main():
    file_handler("input.txt", "output.txt")


if __name__ == "__main__":
    main()
