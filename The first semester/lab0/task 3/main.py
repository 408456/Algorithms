# description: https://drive.google.com/drive/folders/14piLdtzWPQsrT2LqR-i3HxTvN8BUGjmU
def last_digit_of_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, (prev + curr) % 10

    return curr


with open("input.txt", "r") as input_file:
    numbers = input_file.read().strip()
    n_values = list(map(int, numbers.split()))

results = [last_digit_of_fib(n) for n in n_values]

with open("output.txt", "w") as output_file:
    for result in results:
        output_file.write(str(result) + "\n")

print("\n".join(map(str, results)))
