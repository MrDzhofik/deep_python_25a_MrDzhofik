class CustomList(list):
    def __add__(self, other):
        if isinstance(other, (list, CustomList)):
            max_len = max(len(self), len(other))
            new_list = [
                (self[i] if i < len(self) else 0) +
                (other[i] if i < len(other) else 0)
                for i in range(max_len)
            ]
            return CustomList(new_list)
        if isinstance(other, int):
            return CustomList([x + other for x in self])
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, (list, CustomList)):
            max_len = max(len(self), len(other))
            new_list = [
                (self[i] if i < len(self) else 0) -
                (other[i] if i < len(other) else 0)
                for i in range(max_len)
            ]
            return CustomList(new_list)
        if isinstance(other, int):
            return CustomList([x - other for x in self])
        return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, (list, CustomList)):
            max_len = max(len(self), len(other))
            new_list = [
                (other[i] if i < len(other) else 0) -
                (self[i] if i < len(self) else 0)
                for i in range(max_len)
            ]
            return CustomList(new_list)
        if isinstance(other, int):
            return CustomList([other - x for x in self])
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, CustomList):
            return sum(self) == sum(other)
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, CustomList):
            return sum(self) != sum(other)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, CustomList):
            return sum(self) < sum(other)
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, CustomList):
            return sum(self) <= sum(other)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, CustomList):
            return sum(self) > sum(other)
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, CustomList):
            return sum(self) >= sum(other)
        return NotImplemented

    def __str__(self):
        return f"{list(self)}, sum: {sum(self)}"


a = CustomList([5, 1, 3, 7])
b = CustomList([1, 2, 7])
print(a + b)  # [6, 3, 10, 7], sum: 26
print(a - b)  # [4, -1, -4, 7], sum: 6

c = CustomList([10])
d = [2, 5]
print(c + d)  # [12, 5], sum: 17
print(d + c)  # [12, 5], sum: 17

e = CustomList([2, 5])
print(e + 10)  # [12, 15], sum: 27
print(10 + e)  # [12, 15], sum: 27
print(10 - e)  # [8, 5], sum: 13

print(a == b)  # False (26 != 10)
print(a > b)   # True (26 > 10)
print(a < b)   # False
print(c > a)  # False
