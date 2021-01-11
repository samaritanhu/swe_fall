#!/usr/bin/env python
# coding: utf-8
# University of California, Irvine
# Master of Software Engineering, Donald Bren School of Information and Computer Science
# Created by: Xinyi Hu
# Date      : 2020/10/11
# Contact   : xinyih20@uci.edu
# Target    : Implement Depth_first search
# Reference : The algorithm design manual


def depth_first_search(adjaceny_matrix, start_node):
    res = []
    backtrack(adjaceny_matrix, start_node, [0], res)
    return res


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


def backtrack(adjaceny_matrix, start_node, track, res):
    if len(track) == len(adjaceny_matrix):
        res.append(track.copy())
        return

    current_array = transfer_arr_list(adjaceny_matrix[start_node])
    for i in range(len(current_array)):
        if current_array[i] in track:
            continue
        track.append(current_array[i])
        backtrack(adjaceny_matrix, current_array[i], track, res)
        track.pop()