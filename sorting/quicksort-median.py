import statistics
# def median(a, first, last, middle):
#     if a[first] < a[last]:
#         return first if a[middle] < a[first] else middle if a[middle] < a[last] else last
#     else:
#         return last if a[middle] < a[last] else middle if a[middle] < a[first] else first


def quickSort(lst):
    quickSortHelper(lst,0,len(lst) - 1)
    return lst

def quickSortHelper(lst,first,last):
    if first < last:
        splitpoint = partition(lst,first,last)
        quickSortHelper(lst,first,splitpoint - 1)
        quickSortHelper(lst,splitpoint + 1,last)
    


def partition(lst,first,last):
    pivotindex = statistics.median([first, last, (first + last) // 2])
    lst[first], lst[pivotindex] = lst[pivotindex], lst[first]
    pivotvalue = lst[first]
    leftmark = first + 1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and lst[leftmark] <= pivotvalue:
            leftmark += 1
        while lst[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1
        if rightmark < leftmark:
            done = True
        else:
            temp = lst[leftmark]
            lst[leftmark] = lst[rightmark]
            lst[rightmark] = temp

    temp = lst[first]
    lst[first] = lst[rightmark]
    lst[rightmark] = temp


    return rightmark



print(quickSort([232,25,1,4,7]))