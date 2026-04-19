from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value  # key qayta joylashtiradi, shu jumladan oxirgi joyga
            return value
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)  # oxirgi joydagi elementni o'chiradi
        self.cache[key] = value
```

Kodni ishlatish uchun misol:
```python
cache = LRUCache(2)  # cache hajmi 2

cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # 1
cache.put(3, 3)  # 2 o'chiriladi
print(cache.get(2))  # -1
cache.put(4, 4)  # 1 o'chiriladi
print(cache.get(1))  # -1
print(cache.get(3))  # 3
print(cache.get(4))  # 4
