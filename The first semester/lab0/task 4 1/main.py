import time
import psutil
import os


# description: https://drive.google.com/drive/folders/14piLdtzWPQsrT2LqR-i3HxTvN8BUGjmU
def calc_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr

    return curr


def measure_time_for_fib_task_2(n_values):
    start_time = time.perf_counter()

    process = psutil.Process(os.getpid())
    memory_before = process.memory_info().rss / 1024 / 1024  # МБ

    read_start_time = time.perf_counter()
    with open("input.txt", "r") as input_file:
        numbers = input_file.read().strip()
        n_values = list(map(int, numbers.split()))
    read_end_time = time.perf_counter()
    read_time = read_end_time - read_start_time

    write_start_time = time.perf_counter()
    with open("output.txt", "w") as output_file:
        for n in n_values:
            result = calc_fib(n)
            output_file.write(str(result) + "\n")
    write_end_time = time.perf_counter()
    write_time = write_end_time - write_start_time

    memory_after = process.memory_info().rss / 1024 / 1024  # память в МБ

    end_time = time.perf_counter()
    total_time = end_time - start_time
    memory_used = memory_after - memory_before

    print(f"Общее время выполнения: {total_time:.8f} секунд")
    print(f"Время чтения данных: {read_time:.8f} секунд")
    print(f"Время записи данных: {write_time:.8f} секунд")
    print(f"Используемая память: {memory_used:.2f} МБ")


with open("input.txt", "r") as input_file:
    numbers = input_file.read().strip()
    n_values = list(map(int, numbers.split()))

measure_time_for_fib_task_2(n_values)
