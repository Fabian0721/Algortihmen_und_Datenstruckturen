import copy
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

#""" Achtung, damit das Diagramm aus Aufgabe b) zu sehen ist muss dieses # entfernt werden, sowie das andere so gekennzeichente weiter unten
"""Aufgabe a)"""

counterG = 0

def insertionSort(a):
    N = len(a)
    counter = 0
    for i in range(N):
        current = a[i]
        j = i
        while j > 0 and a[j - 1] > current:
            a[j] = a[j - 1]
            counter += 1
            j -= 1
            a[j] = current
    return a, counter

def mergeSort(a):
    return mergeSort_(a,0)

def mergeSort_(a, counter2):
    N = len(a)
    if N <= 1:
        return a, counter2
    else:
        left = a[0:N//2]
        right = a[N//2:N]
        leftSorted, counter2 = mergeSort_(left, counter2)
        rightSorted, counter2 = mergeSort_(right, counter2)
        merged, counter2 = merge(leftSorted, rightSorted, counter2)
        return merged, counter2

def merge(left, right, counter):
    res = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        counter += 1
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i < len(left):
       res.append(left[i])
       i += 1
    while j < len(right):
       res.append(right[j])
       j += 1
    return res, counter


def quickSort(a):
    global counterG
    quickSortImpl(a, 0, len(a)-1)
    return a, counterG

def quickSortImpl(a, l, r):
    """a ist das zu sortierende Array,
       l und r sind die linke und rechte Grenze (inklusive) des zu sortierenden Bereichs"""
    if r > l:
        k = partition(a, l, r)
        quickSortImpl(a, l, k-1)
        quickSortImpl(a, k+1, r)

def partition(a, l, r):
    global counterG
    pivot = a[r]
    i  = l
    j  = r - 1
    while True:
        while i < r and a[i] <= pivot:
            i += 1
        while j > l and a[j] >= pivot:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
            counterG += 1
        else:
            break
    a[r] = a[i]
    a[i] = pivot
    return i

len2 = [ ]
comp1 = [ ]
comp2 = [ ]
comp3 = [ ]

for i in range(1, 101):
    a1 = list(range(i, 0, -1))
    a2 = copy.deepcopy(a1)
    a3 = copy.deepcopy(a1)
    a1, comparisonCount1 = insertionSort(a1)
    a2, comparisonCount2 = mergeSort(a2)
    a3, comparisonCount3 = quickSort(a3)
    comp1.append(comparisonCount1)
    comp2.append(comparisonCount2)
    comp3.append(comparisonCount3)
    len2.append(i)

print(comparisonCount1)
print(comparisonCount2)
print(comparisonCount3)

plt.plot(len2, comp1, 'b')
plt.plot(len2, comp2, 'r')
plt.plot(len2, comp3, 'g')

plt.xlabel("Length")
plt.ylabel("Comparisons")
plt.title("Comparisons depending on Length")
blue_patch = mpatches.Patch(color="blue", label="insertionSort()")
red_patch = mpatches.Patch(color="red", label="mergeSort()")
green_patch = mpatches.Patch(color="green", label="quickSort()")
plt.legend(handles=[blue_patch, red_patch, green_patch])
plt.savefig("comparison.png")
plt.show()

#""" Achtung, damit das Diagramm aus Aufgabe b) zu sehen ist muss dieses # entfernt werden, sowie das andere so gekennzeichente weiter oben
  
"""Aufgabe b)"""

def insertionSort_time(size, counter = 1):
    import timeit
    _insertionSort = insertionSort
    time = timeit.timeit("_insertionSort(list(range(size, 0, -1)))", globals = locals(), number=counter)

    return time / counter

def mergeSort_time(size, counter = 1):
    import timeit
    _mergeSort = mergeSort
    time = timeit.timeit("_mergeSort(list(range(size, 0, -1)))", globals = locals(), number=counter)

    return time / counter

def quickSort_time(size, counter = 1):
    import timeit
    _quickSort = quickSort
    time = timeit.timeit("_quickSort(list(range(size, 0, -1)))", globals = locals(), number=counter)

    return time / counter


def time_graph():
    time1 = [ ]
    time2 = [ ]
    time3 = [ ]
    len1 = [ ]

    for i in range(1, 101):
        time1.append(insertionSort_time(i, 1000))
        time2.append(mergeSort_time(i, 1000))
        time3.append(quickSort_time(i, 1000))
        len1.append(i)

    plt.plot(len1, time1, 'b')
    plt.plot(len1, time2, 'r')
    plt.plot(len1, time3, 'g')

    plt.xlabel("Length")
    plt.ylabel("Time")
    plt.title("Time depending on Length")
    blue_patch = mpatches.Patch(color="blue", label="insertionSort()")
    red_patch = mpatches.Patch(color="red", label="mergeSort()")
    green_patch = mpatches.Patch(color="green", label="quickSort()")
    plt.legend(handles=[blue_patch, red_patch, green_patch])
    plt.savefig("times.png")
    plt.show()

time_graph()

"""Aufgabe c)"""

def rightsort(aBe, aAf):

    if len(aBe) != len(aAf):
        return False

    for i in range(1, len(aAf)-1):
        if aAf[i] > aAf[i+1]:
            return False

    x = set(aBe)
    y = set (aAf)
    if x != y:
        return False
    else:
        return True
