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
        if isinstance(other, (list, CustomList)):
            if len(self) != len(other):
                return False
            for i, _ in enumerate(self):
                if self[i] != other[i]:
                    return False
            return True
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, (list, CustomList)):
            equal = 0
            if len(self) == len(other):
                for i, _ in enumerate(self):
                    if self[i] == other[i]:
                        equal += 1
            return equal != len(self)
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
