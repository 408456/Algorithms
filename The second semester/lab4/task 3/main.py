def rabin_karp_search(pattern, text):
    base = 256
    prime = 101
    m, n = len(pattern), len(text)
    hpattern, htext, h = 0, 0, 1
    result = []

    for i in range(m - 1):
        h = (h * base) % prime

    for i in range(m):
        hpattern = (base * hpattern + ord(pattern[i])) % prime
        htext = (base * htext + ord(text[i])) % prime

    for i in range(n - m + 1):
        if hpattern == htext:
            if text[i:i + m] == pattern:
                result.append(i + 1)

        if i < n - m:
            htext = (base * (htext - ord(text[i]) * h) + ord(text[i + m])) % prime
            if htext < 0:
                htext += prime  # хеш неотрицательный

    return result


def file_handler(input_file, output_file):
    with open(input_file, "r") as file:
        pattern = file.readline().strip()
        text = file.readline().strip()

    matches = rabin_karp_search(pattern, text)

    with open(output_file, "w") as file:
        file.write(f"{len(matches)}\n")
        if matches:
            file.write(" ".join(map(str, matches)) + "\n")


def main():
    file_handler("input.txt", "ouput.txt")


if __name__ == "__main__":
    main()
