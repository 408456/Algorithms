# merge_sort
def merge_two_list(a, b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    c += a[i:]
    c += b[j:]
    return c


def merge_sort(s):
    if len(s) <= 1:
        return s
    middle = len(s) // 2
    left = merge_sort(s[:middle])
    right = merge_sort(s[middle:])
    return merge_two_list(left, right)


s = [7, 5, 2, 3, 9, 8, 6]
print(merge_sort(s))


# Разделяй и властвуй
def bin_search(s, i):
    s.sort()
    start = 0
    finish = len(s) - 1

    while start <= finish:
        middle = (start + finish) // 2
        guess = s[middle]

        if guess == i:
            return True

        if guess > i:
            finish = middle - 1
        else:
            start = middle + 1

    return False


s = [1, 2, 100, 51, 15, 2, 52, 5, 32, 8, 156, 11, 0, 1324]
i = 32
print(bin_search(s, i))

# поиск максимального под массива
i = [1, 2, 3, 4, -5, -9, 0, 100, -99, 51, 55, -35]
o = []


def max_subarray(arr):
    max_sum = arr[0]
    current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray(arr))
