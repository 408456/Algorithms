def rabin_karp_search(s, q, queries):
    m1 = 10 ** 9 + 7
    m2 = 10 ** 9 + 9
    n = len(s)
    x = 31

    s = [ord(c) - ord('a') for c in s]

    # массивы префиксных хешей
    h1 = [0] * (n + 1)
    h2 = [0] * (n + 1)
    # массивы степеней x
    p1 = [1] * (n + 1)
    p2 = [1] * (n + 1)

    # рассчитываем префикс и степени x
    for i in range(1, n + 1):
        h1[i] = (h1[i - 1] * x + s[i - 1]) % m1
        h2[i] = (h2[i - 1] * x + s[i - 1]) % m2
        p1[i] = (p1[i - 1] * x) % m1
        p2[i] = (p2[i - 1] * x) % m2
    result = []

    # хеш подстроки
    for a, b, l in queries:
        hash1_a = (h1[a + l] - h1[a] * p1[l]) % m1
        hash2_a = (h2[a + l] - h2[a] * p2[l]) % m2
        hash1_b = (h1[b + l] - h1[b] * p1[l]) % m1
        hash2_b = (h2[b + l] - h2[b] * p2[l]) % m2

        if hash1_a == hash1_b and hash2_a == hash2_b:
            result.append("Yes")
        else:
            result.append("No")
    return result


def file_handler(input_file, output_file):
    with open(input_file, "r") as file:
        s = file.readline().strip()
        q = int(file.readline())
        queries = [tuple(map(int, file.readline().split())) for _ in range(q)]

    results = rabin_karp_search(s, q, queries)

    with open(output_file, "w") as file:
        file.write("\n".join(results) + "\n")


def main():
    file_handler("input.txt", "output.txt")


if __name__ == "__main__":
    main()
