def add_binary(A, B):
    n = len(A)
    C = [0] * (n + 1)
    carry = 0
    for i in range(n - 1, -1, -1):
        total = int(A[i]) + int(B[i]) + carry
        C[i + 1] = total % 2
        carry = total // 2
    C[0] = carry
    return ''.join(map(str, C))


with open("input.txt", "r") as f:
    A, B = f.read().strip().split()

result = add_binary(A, B)

with open("output.txt", "w") as f:
    f.write(result + "\n")

with open("output.txt", "r") as f:
    print(f.read())
print("Оценка времени работы алгоритма сортировки вставками - O(n)")
