# Быстрая сортировка
# a = [7, 6, 10, 5, 9, 8, 3, 4]
# [6, 5, 3, 4] [7] [10, 9, 8]
def quick_sort(s):
    if len(s) <= 1:
        return s
    elem = s[0]
    left = list(filter(lambda x: x < elem, s))
    middle = list(filter(lambda x: x == elem, s))
    right = list(filter(lambda x: x > elem, s))
    # middle = [i for i in s if i == elem]

    return quick_sort(left) + middle + quick_sort(right)

s = [7, 6, 10, 5, 9, 8, 3, 4]
print(quick_sort(s))

# сортировка за линейное время
#
# индекс хирша - оценка продуктивности научной публикации
# [1, 2, 3, 4]
#
#