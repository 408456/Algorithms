def multiply_poly(A, B):
    n = len(A)
    if n == 1:
        return [A[0] * B[0]]

    mid = n // 2
    A1, A2 = A[:mid], A[mid:]
    B1, B2 = B[:mid], B[mid:]

    D1 = multiply_poly(A1, B1)
    D2 = multiply_poly(A2, B2)
    D3 = multiply_poly([a + b for a, b in zip(A1, A2)],
                       [a + b for a, b in zip(B1, B2)])

    result = [0] * (2 * n - 1)

    for i in range(len(D1)):
        result[i] += D1[i]
    for i in range(len(D2)):
        result[i + 2 * mid] += D2[i]
    for i in range(len(D3)):
        result[i + mid] += D3[i] - D1[i] - D2[i]

    return result


def main():
    with open("input.txt", "r") as file:
        n = int(file.readline().strip())
        A = list(map(int, file.readline().split()))
        B = list(map(int, file.readline().split()))
        print(n, A, B, sep="\n")

    m = 1
    while m < n:
        m *= 2
    A += [0] * (m - n)
    B += [0] * (m - n)

    C = multiply_poly(A, B)

    with open("output.txt", "w") as file:
        file.write(" ".join(map(str, C[:2 * n - 1])))
    with open("output.txt", "r") as f:
        print(f.readline())


if __name__ == "__main__":
    main()
