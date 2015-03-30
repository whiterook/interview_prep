__author__ = 'Sergey'


def sort(lst):
    srt(lst, 0, len(lst)-1)


def srt(lst, low, high):
    if low < high:
        pivot_index = partition(lst, low, high)
        srt(lst, low, pivot_index - 1)
        srt(lst, pivot_index + 1, high)


def partition(lst, low, high):
    l = low
    h = high + 1
    pivot = lst[low]
    while True:
        while True:
            if l == high:
                break
            l += 1
            if lst[l] >= pivot:
                break
        while True:
            if h == low:
                break
            h -= 1
            if lst[h] <= pivot:
                break
        if l >= h:
            break
        swap(lst, l, h)
    swap(lst, low, h)
    return h


def swap(lst, index1, index2):
    tmp = lst[index1]
    lst[index1] = lst[index2]
    lst[index2] = tmp


def main():
    lst = [2, 5, 6, 0, 1, 4]
    print(lst)
    sort(lst)
    print(lst)

if __name__ == '__main__':
    main()