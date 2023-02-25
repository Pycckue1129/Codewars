# You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.
#
# Array can contain numbers or strings. X can be either.
#
# Return true if the array contains the value, false if not.

list1 = ['e', 1, 3, 4, 56, 3, 2, 1]


def check(seq, elem):
    s = bool
    for el in seq:
        if elem == el:
            s = True
            return s
        else:
            s = False
    return s


print(check(list1, 'r'))

