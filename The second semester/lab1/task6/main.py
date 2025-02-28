# Анализ сложности алгоритма: O(n * log n)
# 10 -> "101010" 5 -> "555"
def max_number(num):
    num = sorted(num, key=lambda x: str(x) * 3, reverse=True)
    return "".join(map(str, num))


def file_handler(input_file, output_file):
    with open(input_file, "r") as f:
        n = int(f.readline().strip())
        numbers = list(map(int, f.readline().split()))

    result = max_number(numbers)

    with open(output_file, "w") as f:
        f.write(result + "\n")


def main():
    file_handler("input.txt", "output.txt")


if __name__ == "__main__":
    main()
