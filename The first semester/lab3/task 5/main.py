def quick_sort(s):
    if len(s) <= 1:
        return s
    elem = s[0]
    left = list(filter(lambda x: x < elem, s))
    middle = list(filter(lambda x: x == elem, s))
    right = list(filter(lambda x: x > elem, s))
    return quick_sort(left) + middle + quick_sort(right)


def h_index(citations):
    citations.sort(reverse=True)
    h = 0
    for i, c in enumerate(citations, start=1):
        if c >= i:
            h = i
        else:
            break
    return h


def main():
    with open("input.txt", "r") as f:
        citations = list(map(int, f.readline().replace(",", " ").split()))

    h = h_index(citations)
    print(h)

    with open("output.txt", "w") as f:
        f.write(str(h))


if __name__ == "__main__":
    main()
