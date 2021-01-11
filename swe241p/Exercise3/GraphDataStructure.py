#!/usr/bin/env python
# coding: utf-8
# University of California, Irvine
# Master of Software Engineering, Donald Bren School of Information and Computer Science
# Created by: Xinyi Hu
# Date      : 2020/10/11
# Contact   : xinyih20@uci.edu
# Target    :
# a. Convert from an adjacency matrix to adjacency lists
#
# b. Convert from an adjacency list to an incidence matrix.
# An incidence matrix M has a row for each vertex and a column for each edge,
# such that M[i, j] = 1 if vertex i is part of edge j, otherwise M[i, j] = 0.
#
# c. Convert from an incidence matrix to adjacency lists.
#
# Reference : The algorithm design manual

from LinkedList import LinkedList


def adjaceny_matrix_to_list(adjaceny_matrix):
    adjaceny_list = [LinkedList() for _ in range(len(adjaceny_matrix))]
    for i in range(len(adjaceny_matrix)):
        adjaceny_list[i].add(i)
        for j in range(len(adjaceny_matrix[i])):
            if adjaceny_matrix[i][j] == 1:
                adjaceny_list[i].add(j)
    return adjaceny_list


def adjaceny_list_to_incidence_matrix(adjaceny_list):
    def transfer_list_arr(array, num_vertex):
        # this function transfers
        # [0, 2] into
        # [1, 0, 1]
        # input: int [2]
        # output: int [num_vertex]
        res = [0 for _ in range(num_vertex)]
        for num in array:
            res[num] = 1
        return res

    def drop_duplicates(incidence_matrix):
        temp = []
        for arr in incidence_matrix:
            if arr not in temp:
                temp.append(arr)
        return temp

    num_vertex = len(adjaceny_list)
    incidence_matrix = []
    for i, adjaceny_ll in enumerate(adjaceny_list):
        current_ll = adjaceny_ll.head.next
        current_data = current_ll.data
        while current_data is not None:
            incidence_matrix.append(transfer_list_arr([i, current_data], num_vertex))
            if current_ll.next:
                current_ll = current_ll.next
                current_data = current_ll.data
            else:
                current_data = None

    return drop_duplicates(incidence_matrix)


def incidence_matrix_to_adjaceny_list(incidence_matrix):
    def transfer_arr_list(array):
        # this function transfers
        # [1, 0, 1] into
        # [0, 2]
        # input: int [num_vertex]
        # output: int [2]
        res = []
        for i, num in enumerate(array):
            if num == 1:
                res.append(i)
        return res

    num_vertex = len(incidence_matrix[0])
    adjaceny_list = [LinkedList() for i in range(num_vertex)]
    [l.add(i) for i, l in enumerate(adjaceny_list)]
    for each_line in incidence_matrix:
        array = transfer_arr_list(each_line)
        adjaceny_list[array[0]].add(array[1])
        adjaceny_list[array[1]].add(array[0])
    return adjaceny_list