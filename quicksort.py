__author__ = 'Daan Debie'

def quicksort(l):
    if not l:
        return []
    lesser = []
    greater = []
    pivot = l[0]
    for i in l[1:]:
        if i >= pivot:
            greater.append(i)
        if i < pivot:
            lesser.append(i)
    return quicksort(lesser) + [pivot] + quicksort(greater)

numbers = [52, 66, 50, 21, 91, 52, 63, 48, 6, 78, 74]
n = quicksort(numbers)

print n