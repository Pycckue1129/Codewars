# You get an array of numbers, return the sum of all of the positives ones.
#
# Example [1,-4,7,12] => 1 + 7 + 12 = 20
#
# Note: if there is nothing to sum, the sum is default to 0.

def positive_sum(arr):
    # Your code here
    summ = 0
    if len(arr) == 0:
        return 0
    for el in arr:
        if el >= 0:
            summ += el
    return summ


list1 = [1, -4, 7, 12, 0, -2, 2]
print(positive_sum(list1))
