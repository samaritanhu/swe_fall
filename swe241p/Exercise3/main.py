#!/usr/bin/env python
# coding: utf-8
# University of California, Irvine
# Master of Software Engineering, Donald Bren School of Information and Computer Science
# Created by: Xinyi Hu
# Date      : 2020/10/11
# Contact   : xinyih20@uci.edu
# Target    :
# Note: This is the main file to test all of the sub-files
#
# a. Convert from an adjacency matrix to adjacency lists
#
# b. Convert from an adjacency list to an incidence matrix.
# An incidence matrix M has a row for each vertex and a column for each edge,
# such that M[i, j] = 1 if vertex i is part of edge j, otherwise M[i, j] = 0.
#
# c. Convert from an incidence matrix to adjacency lists.
#
# Reference : The algorithm design manual

from GraphDataStructure import *


def run():
    adjaceny_matrix = [[0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0],
                  [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0,],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0]]  # adjacency matrix
    adjaceny_list = adjaceny_matrix_to_list(adjaceny_matrix)
    print('Adjacency List:')
    for eachll in adjaceny_list:
        eachll.print()

    incidence_matrix = adjaceny_list_to_incidence_matrix(adjaceny_list)
    print('Incidence Matrix:\n', incidence_matrix)

    al = incidence_matrix_to_adjaceny_list(incidence_matrix)
    print('Adjacency List:')
    for eachll in al:
        eachll.print()


if __name__ == '__main__':
    run()
