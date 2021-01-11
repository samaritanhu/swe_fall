#!/usr/bin/env python
# coding: utf-8
# University of California, Irvine
# Master of Software Engineering, Donald Bren School of Information and Computer Science
# Created by: Xinyi Hu
# Date      : 2020/10/09
# Contact   : xinyih20@uci.edu
# Target    : Realize InsertionSort
# Reference : The algorithm design manual


class InsertionSort:
    def __init__(self, arr):
        self.arr = arr

    def SortingProcess(self):
        for i in range(len(self.arr)):
            j = i
            while (self.arr[j] < self.arr[j - 1]) and j > 0:
                self.arr[j], self.arr[j - 1] = self.arr[j - 1], self.arr[j]
                j = j - 1
        return

    def SortingProcess2(self):
        for i in range(1, len(self.arr)):
            current = self.arr[i]
            pre_index = i - 1
            while pre_index >= 0 and self.arr[pre_index] > current:
                self.arr[pre_index + 1] = self.arr[pre_index]
                pre_index -= 1
            self.arr[pre_index + 1] = current

    def PrintOutput(self):
        print(self.arr)


if __name__ == "__main__":
    arr = [2, 5, 3, 1, 10, 4]
    ISort = InsertionSort(arr)
    ISort.SortingProcess2()
    ISort.PrintOutput()