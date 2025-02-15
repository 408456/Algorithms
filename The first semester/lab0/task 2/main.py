# description: https://drive.google.com/drive/folders/14piLdtzWPQsrT2LqR-i3HxTvN8BUGjmU
def calc_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        # сумма двух предыдущих чисел
        prev, curr = curr, prev + curr

    return curr


with open("input.txt", "r") as input_file:
    numbers = input_file.read().strip()
    n_values = list(map(int, numbers.split()))

with open("output.txt", "w") as output_file:
    for n in n_values:
        result = calc_fib(n)
        output_file.write(str(result) + "\n")

with open("output.txt", "r") as output_file_for_reading:
    print(output_file_for_reading.read())
