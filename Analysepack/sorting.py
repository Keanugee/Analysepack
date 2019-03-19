#Bubble Sort
def bubble_sort(items):
    length = len(items) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            if items[i] > items[i+1]:
                sorted = False
                items[i], items[i+1] = items[i+1], items[i]
    return items

#Merge Sort
def merge_sort(items):

    len_i = len(items)
    # Base case. A list of size 1 is sorted.
    # Cae returns, so if reached then function will terminate after line 8
    if len_i == 1:
        return items
    # Recursive case. Find midpoint of list
    mid_point = int(len_i / 2)
    # divide list into two halves
    i1 = merge_sort(items[:mid_point])
    i2 = merge_sort(items[mid_point:])
    # call merge_sort function on each half of list
    return merge(i1, i2)
# Merge function.
def merge(A, B):
    new_list = []
    while len(A) > 0 and len(B) > 0:
        if A[0] < B[0]:
            new_list.append(A[0])
            A.pop(0)
        else:
            new_list.append(B[0])
            B.pop(0)

    if len(A) == 0:
        new_list = new_list + B
    if len(B) == 0:
        new_list = new_list + A

    return new_list

#Quick Sort
def quick_sort(items):
    if len(items) <= 1:
        return items
    else:
        return quick_sort([x for x in items[1:] if x < items[0]])\
         + [items[0]]\
         + quick_sort([x for x in items[1:] if x >= items[0]])
