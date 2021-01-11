#!/usr/bin/env python
# coding: utf-8
# University of California, Irvine
# Master of Software Engineering, Donald Bren School of Information and Computer Science
# Created by: Xinyi Hu
# Date      : 2020/10/11
# Contact   : xinyih20@uci.edu
# Target    : Implement Breath_first search
# Reference : The algorithm design manual

from DepthFirstSearch import transfer_arr_list


def breath_first_search(adjaceny_matrix, start_node):
    queue = [start_node]
    visited = []
    while queue:
        a = queue.pop(0)
        if a not in visited:
            visited.append(a)
            for x in transfer_arr_list(adjaceny_matrix[a]):
                if x not in visited:
                    queue.append(x)
    return visited

