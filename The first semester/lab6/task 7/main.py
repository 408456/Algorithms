def file_handler(input_file, output_file):
    with open(input_file, "r") as fin:
        n, k = map(int, fin.readline().split())
        s = fin.readline().strip()
        pairs = [fin.readline().strip() for _ in range(k)]

    result = beautiful_pairs(n, s, pairs)

    with open(output_file, "w") as out:
        out.write(str(result) + '\n')


def beautiful_pairs(n, s, pairs):
    pair_dict = {chr(i): set() for i in range(ord('a'), ord('z') + 1)}

    for p in pairs:
        a, b = p
        pair_dict[a].add(b)

    count = 0
    letter_count = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}

    for i in range(n - 1, -1, -1):
        c = s[i]
        for b in pair_dict[c]:
            count += letter_count[b]
        letter_count[c] += 1

    return count


def main():
    file_handler("input.txt", "output.txt")


if __name__ == "__main__":
    main()
