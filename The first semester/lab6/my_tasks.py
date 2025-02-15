# h(u) = (a * u mod p) mod 9
# a - 44, u - 6 вариант, p - 31

# h(u) = ((a * u + b) mod p) mod 9
# гольцман. Сумма: sum(ord(letter) for letter in surname)

A = 44
U = 6
P = 31


def hash_task_1(a, u, p):
    return (a * u % p) % 9


def hash_task_2(a, u, p, b):
    return ((a * u + b) % p) % 9 + 1


surname = "Гольцман"
B = sum(ord(letter) for letter in surname)

task_1 = hash_task_1(A, U, P)
task_2 = hash_task_2(A, U, P, B)
task_3 = 1

print(task_3, task_2, task_1)
