#!/usr/bin/env python
# coding: utf-8
# University of California, Irvine
# Master of Software Engineering, Donald Bren School of Information and Computer Science
# Created by: Xinyi Hu
# Date      : 2020/10/09
# Contact   : xinyih20@uci.edu
# Target    : Realize QuickSort
# Reference : The algorithm design manual

import random


class QuickSort:
    def __init__(self, arr):
        self.original_arr = arr
        self.arr = arr

    def SortingProcess(self, default=''):
        if default == '':
            self.quicksort(0, len(self.arr) - 1)
        elif default == 'random':
            self.quicksort_random(0, len(self.arr) - 1)

    def quicksort(self, l, h):
        if h > l:
            p = self.partition(l, h)
            self.quicksort(l, p - 1)
            self.quicksort(p + 1, h)

    def quicksort_random(self, l, h):
        if h > l:
            p = self.partition_random(l, h)
            self.quicksort_random(l, p - 1)
            self.quicksort_random(p + 1, h)

    def partition(self, l, h):
        p = h
        firsthigh = l
        for i in range(l, h):
            if self.arr[i] < self.arr[p]:
                self.arr[i], self.arr[firsthigh] = self.arr[firsthigh], self.arr[i]
                firsthigh += 1
        self.arr[p], self.arr[firsthigh] = self.arr[firsthigh], self.arr[p]
        return firsthigh

    def partition_random(self, l, h):
        randpivot = random.randrange(l, h)
        self.arr[l], self.arr[randpivot] = self.arr[randpivot], self.arr[l]
        return self.partition(l, h)

    def PrintOutput(self):
        print(self.arr)


def run():
    def quicksort(s, l, h):
        if h > l:
            p = partition(s, l, h)
            quicksort(s, l, p - 1)
            quicksort(s, p + 1, h)

    def partition(s, l, h):
        p = h
        firsthigh = l
        for i in range(l, h):
            if s[i] < s[p]:
                s[i], s[firsthigh] = s[firsthigh], s[i]
                firsthigh += 1
        s[p], s[firsthigh] = s[firsthigh], s[p]
        return firsthigh

    arr = [2, 5, 1, 7, 9, 12, 11, 10]
    quicksort(arr, 0, len(arr) - 1)
    print(arr)


if __name__ == "__main__":
    arr = [2, 5, 1, 7, 9, 12, 11, 10]
    QSort = QuickSort(arr)
    QSort.SortingProcess(default='random')
    QSort.PrintOutput()