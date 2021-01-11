#!/usr/bin/env python
# coding: utf-8
# University of California, Irvine
# Master of Software Engineering, Donald Bren School of Information and Computer Science
# Created by: Xinyi Hu
# Date      : 2020/10/07
# Contact   : xinyih20@uci.edu
# Target    : Using Linked list, Binary Tree and Hash Table to read word from txt file
# Reference : The algorithm design manual

import LinkedList
import BinaryTree
import HashTable
import re
import time


def insert_data(text, filepath, outputname=''):
    SumTime = 0
    output = open(outputname+'.txt', 'w')
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            line = fp.readline()
            # for word in re.split(' |-', line.strip()):
            for word in re.split(r'[^a-z|A-Z|\d+]', line.strip()):
                # word = re.sub('[^a-z|A-Z|\d+]', '', word)
                if word != '':
                    Starttime = time.time_ns()
                    text.add(word)
                    Endtime = time.time_ns()
                    output.write(str(Endtime - Starttime) + ' \n')
                    SumTime += Endtime - Starttime
    output.close()
    print('Total time of inserting words is :', str(SumTime))
    print('Number of words is :', str(text.size()))


def search_data(text, filepath, outputname=''):
    SumTime = 0
    notexist = 0
    output = open(outputname + '.txt', 'w')
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            line = fp.readline()
            for word in line.strip().split(' '):
                word = re.sub('[^a-z|A-Z|\d+]', '', word)
                if word != '':
                    Starttime = time.time_ns()
                    result = text.contains(word)
                    Endtime = time.time_ns()
                    if not result:
                        notexist += 1
                    output.write(str(Endtime - Starttime) + ' \n')
                    SumTime += Endtime - Starttime
    output.close()
    print('Total time of searching words is :', str(SumTime))
    print('Words not found is :', str(notexist))


def run():
    fileinsert = "pride-and-prejudice.txt"
    filesearch = "words-shuffled.txt"
    BinaryTreeText = BinaryTree.BinaryTreeSet()
    print('Binary Tree')
    insert_data(BinaryTreeText, fileinsert, 'insert_bt')
    search_data(BinaryTreeText, filesearch, 'search_bt')

    print('Hash Table')
    HashTableText = HashTable.HashTableSet()
    insert_data(HashTableText, fileinsert, 'insert_ht')
    search_data(HashTableText, filesearch, 'search_ht')

    print('Linked List')
    LinkedListText = LinkedList.LinkedListSet()
    insert_data(LinkedListText, fileinsert, 'insert_ll')
    search_data(LinkedListText, filesearch, 'search_ll')


if __name__ == "__main__":
    run()
