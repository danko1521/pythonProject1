nested_list = [
    ['a', 'b', False, 'c', 'gig', [12, 13]],
    ['d', 'e', 'f', 'h', False],
    ['p', 'i', 'g', 'g'],
    [1, 2, 3, 4, 5]
]

############################################Iterator###################################################################
class Qwerty:

    def __init__(self):
        self.list = nested_list

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        self.count += 1
        for some_list in nested_list:
            for elem in some_list:
                if bool(elem) in some_list:
                    elem = str(elem)
                for el in elem:
                    print(el)

        flattened = [elem for list in nested_list for elem in list]
        print(flattened)
        raise StopIteration


List_iter = Qwerty()
for reading in List_iter:
    print(reading)

print('<><><><><><><><><><><><><><><><><><><><><><>')


def some_list_of_list(nested_list):
    for some_list in nested_list:
        for elem in some_list:
            if bool(elem) in some_list:
                elem = str(elem)
            for el in elem:
                yield el

for item in some_list_of_list(nested_list):
    print(item)

############################################Generator###################################################################