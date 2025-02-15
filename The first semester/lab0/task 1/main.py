# description: https://drive.google.com/drive/folders/14piLdtzWPQsrT2LqR-i3HxTvN8BUGjmU

# Задание №1. Ввод - вывод
a = 10
b = 2
# a, b = map(int, input().split())
print(a + b)

# a, b = map(int, input().split())
print(a + b ** 2)


with open("input.txt", "r") as input_file:
    numbers = input_file.readlines()

with open("output.txt", "w") as output_file:
    for line in numbers:
        a, b = map(int, line.split())
        output_file.write(str(a + b))

with open("output.txt", "r") as output_file_for_reading:
    print(output_file_for_reading.read())

with open("output.txt", "w") as output_file:
    for line in numbers:
        a, b = map(int, line.split())
        output_file.write(str(a + b ** 2))

with open("output.txt", "r") as output_file_for_reading:
    print(output_file_for_reading.read())

