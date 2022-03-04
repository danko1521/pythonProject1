nested_list = [
    ['a', 'b', 'c'], [1, 2, 3, 4, 5, 6, 7, 8], ['d', 'e', 'f', 'h', False], ['d', 'e', 'f', 'h', False], [1, 2, None]
]


class flat_list:

    def __init__(self):
        self.list = nested_list
        self.flat_list = []

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        self.count += 1
        flat_list = []

        for element in nested_list:
            if type(element) is list:

                for item in element:
                    flat_list.append(item)
            else:
                flat_list.append(element)
        return flat_list


List_iter = flat_list()
for reading in List_iter:
    print(reading)
    break

print('<><><><><><><><><><><><><><><><><><><><><><>')


def flat_list_yeld():
    for element in nested_list:
        if isinstance(element, list):
            for item in element:
                yield item
        else:
            yield element


for item in flat_list_yeld():
    print(item)
