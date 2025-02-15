# Хеширование O(1) contains
# backed
hash_set = set()
hash_set.add("Миша")
hash_table = {}
hash_table['яблоки'] = 1.99  # Вставка ключ-значение
hash_table['бананы'] = 0.99
print(hash_table.get('яблоки', 'Нет в наличии'))  # Поиск
hash_table.pop('яблоки')


def hash_function(key, size):
    return key % size


size = 10
print(hash_function(25, size))


# Chaining
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # Список списков

    def insert(self, key, value):
        index = hash_function(key, self.size)
        self.table[index].append((key, value))

    def search(self, key):
        index = hash_function(key, self.size)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = hash_function(key, self.size)
        self.table[index] = [(k, v) for k, v in self.table[index] if k != key]


ht = HashTable(10)
ht.insert(15, 'яблоко')
print(ht.search(15))
ht.delete(15)
print(ht.search(15))
