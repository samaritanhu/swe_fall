#!/usr/bin/env python
# coding: utf-8
# University of California, Irvine
# Master of Software Engineering, Donald Bren School of Information and Computer Science
# Created by: Xinyi Hu
# Date      : 2020/10/07
# Contact   : xinyih20@uci.edu
# Target    : Implement Selection sort, Insertion sort, Heapsort, Mergesort, Quicksort
# Reference : The algorithm design manual

from SelectionSort import SelectionSort
from InsertionSort import InsertionSort
from HeapSort import HeapSort
from MergeSort import MergeSort
from QuickSort import QuickSort
import re
import time
import sys

sys.setrecursionlimit(1000000)


def read_data(filepath):
    words = []
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            line = fp.readline()
            for word in re.split(r'[^a-z|A-Z|\d+]', line.strip()):
                if word != '':
                    words.append(word)
    return words


def run():
    filepath = "pride-and-prejudice.txt"
    words = read_data(filepath)

    # SSort = SelectionSort(words)
    # Starttime = time.time_ns()
    # SSort.SortingProcess()
    # Endtime = time.time_ns()
    # print(Endtime-Starttime)
    #
    # ISort = InsertionSort(words)
    # Starttime = time.time_ns()
    # ISort.SortingProcess2()
    # Endtime = time.time_ns()
    # print(Endtime - Starttime)
    #
    # HSort = HeapSort(words)
    # Starttime = time.time_ns()
    # HSort.SortingProcess()
    # Endtime = time.time_ns()
    # print(Endtime - Starttime)
    #
    # MSort = MergeSort(words)
    # Starttime = time.time_ns()
    # MSort.SortingProcess()
    # Endtime = time.time_ns()
    # print(Endtime - Starttime)

    QSort = QuickSort(words)
    Starttime = time.time_ns()
    QSort.SortingProcess(default='random')
    Endtime = time.time_ns()
    print(Endtime - Starttime)


if __name__ == '__main__':
    run()