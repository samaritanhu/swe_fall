#!/usr/bin/env python
# coding: utf-8
# University of California, Irvine
# Master of Software Engineering, Donald Bren School of Information and Computer Science
# Created by: Xinyi Hu
# Date      : 2020/10/09
# Contact   : xinyih20@uci.edu
# Target    : Realize Selection sort
# Reference : The algorithm design manual


class SelectionSort:
    def __init__(self, arr):
        self.original_arr = arr
        self.arr = arr

    def SortingProcess(self):
        self.sorted = []
        for i in range(len(self.arr)):
            minimum = self.arr[0]
            index = 0
            for j, num in enumerate(self.arr):
                if num < minimum:
                    minimum = num
                    index = j
            self.sorted.append(minimum)
            self.arr = self.arr[:index] + self.arr[index + 1:]
        return

    def PrintOutput(self):
        print(self.sorted)


if __name__ == "__main__":
    arr = [4, 3, 3]
    SSort = SelectionSort(arr)
    SSort.SortingProcess()
    SSort.PrintOutput()