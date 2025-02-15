def generate_fibonacci(limit):
    fib_set = set()
    a, b = 1, 1
    while a <= limit:
        fib_set.add(a)
        a, b = b, a + b
    return fib_set


def file_handler(input_file, output_file):
    fib_set = generate_fibonacci(10 ** 10)  # Генерируем все числа Фибоначчи один раз
    with open(input_file, "r") as fin, open(output_file, "w") as fout:
        N = int(fin.readline().strip())
        for _ in range(N):
            number = int(fin.readline().strip())
            fout.write("Yes\n" if number in fib_set else "No\n")


def main():
    file_handler("input.txt", "output.txt")


if __name__ == "__main__":
    main()
