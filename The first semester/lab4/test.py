# Структуры данных python
import array

arr = array.array('i', [1, 2, 3, 4, 5])  # 'i' означает, что массив хранит целые числа
print(arr)  # array('i', [1, 2, 3, 4, 5])
# 'b' — signed char (целые числа от -128 до 127)
# 'B' — unsigned char (от 0 до 255)
# 'i' — signed int
# 'I' — unsigned int
# 'f' — float
# 'd' — double

lst = [1, 2, 3, "hello", [5, 6]]
# это изменяемые последовательности, динамические массивы, которые могут содержать элементы любых типов.
# append(x)	Добавляет x в конец списка
# extend(iterable)	Добавляет элементы из iterable
# insert(i, x)	Вставляет x на позицию i
# remove(x)	Удаляет первое вхождение x
# pop([i])	Удаляет и возвращает элемент i (или последний)
# index(x, [start, end])	Возвращает индекс x
# count(x)	Количество вхождений x
# sort([key, reverse])	Сортирует список
# reverse()	Разворачивает список
# copy()	Возвращает копию списка
# clear()	Очищает список

tpl = (1, 2, 3, "hello")
# неизменяемые последовательности
# count(x)	Количество элементов x в кортеже
# index(x)	Индекс первого вхождения x

d = {"name": "Alice", "age": 25}
# keys()	Возвращает все ключи
# values()	Возвращает все значения
# items()	Возвращает пары (ключ, значение)
# get(key, default)	Получает значение по ключу
# pop(key, default)	Удаляет ключ и возвращает значение
# popitem()	Удаляет случайную пару
# update(other_dict)	Обновляет словарь
# setdefault(key, default)	Возвращает значение, если ключ есть, иначе добавляет ключ с default
# clear()	Очищает словарь

st = {1, 2, 3, 4, 5}
# это неупорядоченные коллекции уникальных элементов
# add(x)	Добавляет x
# remove(x)	Удаляет x, вызывает ошибку, если нет
# discard(x)	Удаляет x, без ошибки если нет
# pop()	Удаляет случайный элемент
# clear()	Очищает множество
# union(other)	Объединяет множества
# intersection(other)	Пересечение
# difference(other)	Разность
# symmetric_difference(other)	Симметрическая разность
# issubset(other)	Проверяет, является ли подмножеством
# issuperset(other)	Проверяет, является ли надмножеством

# Стек и очередь
# Динамическое множество, работающее по принципу LIFO (Last In, First Out – "последним пришел, первым ушел").
# push(x) — добавление элемента в стек.
# pop() — удаление верхнего элемента.
# peek() — просмотр верхнего элемента (без удаления).
stack = []  # создаем пустой стек
stack.append(2)
print(stack.pop())  # ???
print(type(stack))
from collections import deque

stack = deque()
stack.append(1)
print(stack)

# Очередь — структура данных, работающая по принципу FIFO (First In, First Out – "первым пришел, первым ушел").
# Операции:
#
# enqueue(x) — добавление элемента в конец.
# dequeue() — удаление элемента из начала.
from collections import deque

queue = deque()
queue.append(3)

print(queue.popleft())
print(queue)


class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    def is_empty(self) -> bool:
        if len(self.stack) == 0:
            return True
        return False

# Связные списки - динамическое множество, узлы, содержащее указатели на след и пред элем, порядок определяется указателями
