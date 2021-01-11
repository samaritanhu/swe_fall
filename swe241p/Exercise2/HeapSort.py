#!/usr/bin/env python
# coding: utf-8
# University of California, Irvine
# Master of Software Engineering, Donald Bren School of Information and Computer Science
# Created by: Xinyi Hu
# Date      : 2020/10/09
# Contact   : xinyih20@uci.edu
# Target    : Realize HeapSort
# Reference : The algorithm design manual


'''
a heap-labeled tree is defined to be a binary tree such that
the key labeling of each node dominates the key labeling of each of its children.

In a min-heap, a node dominates its children by containing a smaller key than they do,
while in a max-heap parent nodes dominate by being bigger.
'''


class HeapSort:
    def __init__(self, arr):
        self.original_arr = arr
        self.tree = arr
        self.length = len(arr)

    def heapify(self, n, i):
        if i >= n:
            return
        c1 = 2 * i + 1
        c2 = 2 * i + 2
        max_ = i
        if c1 < n and self.tree[c1] > self.tree[max_]:
            max_ = c1
        if c2 < n and self.tree[c2] > self.tree[max_]:
            max_ = c2
        if max_ != i:
            self.tree[max_], self.tree[i] = self.tree[i], self.tree[max_]
            self.heapify(n, max_)

    def build_heap(self, n):
        last_node = n - 1
        parent = (last_node - 1) // 2
        for i in range(parent, -1, -1):
            self.heapify(n, i)

    def heapsort(self, n):
        self.build_heap(n)
        for i in range(n - 1, -1, -1):
            self.tree[i], self.tree[0] = self.tree[0], self.tree[i]
            self.heapify(i, 0)

    def SortingProcess(self):
        self.heapsort(self.length)

    def PrintOutput(self):
        print(self.tree)


if __name__ == "__main__":
    tree = [2, 5, 3, 1, 10, 4]
    HSort = HeapSort(tree)
    HSort.SortingProcess()
    HSort.PrintOutput()