nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

nested_list_N = [
    ['a', 'b', 'c', [5, 4, [3, 11, [12, 14]]]],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

class FlatIterator:
    def __init__(self, nested_list):
        self.nested_list = nested_list
        self.count_big = 0
        self.count_mini = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count_big < len(nested_list):
            if self.count_mini < len(nested_list[self.count_big])-1:
                res = nested_list[self.count_big][self.count_mini]
                self.count_mini += 1
            else:
                res = nested_list[self.count_big][self.count_mini]
                self.count_big += 1
                self.count_mini = 0
            return res
        else:
            raise StopIteration


class FlatIterator_N:
    def __init__(self, nested_list_N):
        self.nested_list = nested_list_N

    def __iter__(self):
        self.stek_items = [iter(self.nested_list)]
        return self

    def __next__(self):
        while len(self.stek_items) != 0:
            try:
                value = next(self.stek_items[-1])
            except StopIteration:
                self.stek_items.pop()
                continue
            if isinstance(value, list):
                self.stek_items.append(iter(value))
            else:
                return value
        raise StopIteration


def flat_generator(nested_list):
    count_big = 0
    count_mini = 0
    while count_big < len(nested_list):
        while count_mini < len(nested_list[count_big]):
            yield nested_list[count_big][count_mini]
            count_mini += 1
        count_big += 1
        count_mini = 0


def flat_generator_N(nested_list_N):
    for i in nested_list_N:
        if isinstance(i, list):
            for item in flat_generator_N(i):
                yield item
        else:
            yield i


if __name__ == "__main__":
    for it1 in FlatIterator(nested_list):
        print(it1)
    print("*" * 50)
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
    print("--" * 50)

    for it2 in FlatIterator_N(nested_list_N):
        print(it2)
    print("--" * 50)

    for it3 in flat_generator(nested_list):
        print(it3)
    print("--" * 50)

    for it4 in flat_generator_N(nested_list_N):
        print(it4)

