def median(a, i, j, k):
    if a[i] < a[j]:
        return i if a[k] < a[i] else k if a[k] < a[j] else j
    else:
        return j if a[k] < a[j] else k if a[k] < a[i] else i

def quickSort(alist):
    quickSortHelper(alist,0,len(alist) - 1)
    return alist

def quickSortHelper(alist,first,last):
    if first<last:
        splitpoint = partition(alist,first,last)

        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)
    


def partition(alist,first,last):
    pivotvalue = alist[first]
    pivotindex = median(alist, first, last, (first + last) // 2)
    alist[first], alist[pivotindex] = alist[pivotindex], alist[first]
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1
        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp


    return rightmark



print(quickSort([232,25,1,4,7]))