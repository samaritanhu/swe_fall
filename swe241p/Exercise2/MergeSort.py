#!/usr/bin/env python
# coding: utf-8
# University of California, Irvine
# Master of Software Engineering, Donald Bren School of Information and Computer Science
# Created by: Xinyi Hu
# Date      : 2020/10/09
# Contact   : xinyih20@uci.edu
# Target    : Realize MergeSort
# Reference : The algorithm design manual


class MergeSort:
    def __init__(self, arr):
        self.original_arr = arr
        self.arr = arr

    def SortingProcess(self):
        self.mergesort(0, len(self.arr) - 1)

    def mergesort(self, low, high):
        #         if len(self.arr) < 2:
        #             return
        if low < high:
            middle = low + (high - low) // 2
            self.mergesort(low, middle)
            self.mergesort(middle + 1, high)
            self.merge(low, middle, high)

    def merge(self, low, middle, high):
        # print(self.arr[low:high])
        buffer1 = self.arr[low: middle + 1]
        buffer2 = self.arr[middle + 1: high + 1]

        i, j = 0, 0
        result = []
        while i < len(buffer1) and j < len(buffer2):
            if buffer1[i] > buffer2[j]:
                result.append(buffer2[j])
                j += 1
            else:
                result.append(buffer1[i])
                i += 1

        result += buffer1[i:]
        result += buffer2[j:]
        self.arr[low:high + 1] = result
        # print(self.arr[low:high + 1])

    def PrintOutput(self):
        print(self.arr)


class MergeSort2:
    def __init__(self, arr):
        self.original_arr = arr
        self.arr = arr

    def SortingProcess(self):
        self.arr = self.mergesort(self.arr)

    def mergesort(self, array):
        if len(array) < 2:
            return array
        middle = len(array) // 2
        left = self.mergesort(array[:middle])
        right = self.mergesort(array[middle:])
        res = self.merge(left, right)
        return res

    def merge(self, left, right):
        i, j = 0, 0
        result = []
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                result.append(right[j])
                j += 1
            else:
                result.append(left[i])
                i += 1

        result += left[i:]
        result += right[j:]
        return result

    def PrintOutput(self):
        print(self.arr)


if __name__ == "__main__":
    arr = [1, 4, 3, 5, 2]
    MSort = MergeSort2(arr)
    MSort.SortingProcess()
    MSort.PrintOutput()