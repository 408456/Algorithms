# Жадные алгоритмы. Динамическое программирование №2
# задача с заправками
def min_refills(D, L, stations):
    stations.append(D)
    current_fuel = L
    position = 0
    refills = 0
    i = 0

    while position < D:
        last_position = position

        while i < len(stations) and stations[i] - position <= current_fuel:
            last_position = stations[i]
            i += 1

        if last_position == position:
            return -1

        if last_position < D:
            refills += 1

        position = last_position
        current_fuel = L

    return refills


D = 500
L = 200
stations = [100, 200, 300, 400]
print(min_refills(D, L, stations), "O(n)")


# задача с рюкзаком
def knapsack(C, items):
    items.sort(key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0
    for weight, value in items:
        if C >= weight:
            C -= weight
            total_value += value
    return total_value


items = [(10, 60), (20, 100), (30, 120)]
C = 50
print(knapsack(C, items))

#
num = [1, 2, 4, 9, 1, 9, 3]


def max_number(num):
    num = sorted(num, key=lambda x: str(x) * 10, reverse=True)
    result = "".join(map(str, num))
    return result

num = [3, 30, 34, 5, 9]
print(max_number(num))
#
