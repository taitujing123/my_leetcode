import numpy as np

"""
冒泡排序（Bubble Sort）也是一种简单直观的排序算法。
它重复地走访过要排序的数列，一次比较两个元素，如果他们
的顺序错误就把他们交换过来。走访数列的工作是重复地进行
直到没有再需要交换，也就是说该数列已经排序完成。这个算法
的名字由来是因为越小的元素会经由交换慢慢"浮"到数列的顶端。
"""
def bubbleSort(a):
    n = len(a)
    for i in range(n):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

"""
插入排序（英语：Insertion Sort）是一种简单直观的
排序算法。它的工作原理是通过构建有序序列，对于未排序
数据，在已排序序列中从后向前扫描，找到相应位置并插入。
"""
def insertSort(a):
    n = len(a)
    for i in range(1,n):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a

"""
快速排序使用分治法（Divide and conquer）策略来把一个序列（list）分为较小和较大的2
个子序列，然后递归地排序两个子序列。
步骤为：
挑选基准值：从数列中挑出一个元素，称为"基准"（pivot）;
分割：重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准后面
（与基准值相等的数可以到任何一边）。在这个分割结束之后，对基准值的排序就已经完成;
递归排序子序列：递归地将小于基准值元素的子序列和大于基准值元素的子序列排序。
递归到最底部的判断条件是数列的大小是零或一，此时该数列显然已经有序。

选取基准值有数种具体方法，此选取方法对排序的时间性能有决定性影响。
"""
def partition(arr,low,high):
    i = low - 1 #最小元素索引
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

# arr[] --> 排序数组
# low  --> 起始索引
# high  --> 结束索引

def quickSort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)

        quickSort(arr, low, pivot-1)
        quickSort(arr, pivot+1, high)

    return arr

def selectSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    #创建临时数组
    L = [0] * n1
    R = [0] * n2

    #拷贝数据到临时数组
    for i in range(n1):
        L[i] = arr[l+i]
    for i in range(n2):
        R[i] = arr[m+1+i]

    #归并临时数组到原数组
    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    #拷贝L剩余元素
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    #拷贝R剩余元素
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if l < r:
        m = int((l+r-1) / 2)
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

    return arr


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 交换

        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    #build a maxheap
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    #一个个交换元素
    for i in range(n-1,0,-1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


if __name__ == "__main__":

    x = [32, 2, 4, 24, 65, 34, 1, 8, 6, 55, 73]

    print(heapSort(x))