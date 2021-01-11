#!/usr/bin/env python
# coding: utf-8
# University of California, Irvine
# Master of Software Engineering, Donald Bren School of Information and Computer Science
# Created by: Xinyi Hu
# Date      : 2020/10/07
# Contact   : xinyih20@uci.edu
# Target    : Realize Hash Table by scratch in Python
# Reference : The algorithm design manual

from LinkedList import LinkedList
# hashcode reference: https://blog.csdn.net/hongxingabc/article/details/82891503
def hashCode(s):
    seed = 31
    h = 0
    for c in s:
        h = int32(seed * h) + ord(c)
    return h


class HashTable:
    def __init__(self, hashsize=10000):
        self.size = 0
        self.hashsize = hashsize
        self.hashlist = [None for _ in range(hashsize)]

    def add(self, data):
        hashcodeData = hash(data)
        arrayIndex = abs(hashcodeData) % self.hashsize
        if self.hashlist[arrayIndex] is None:
            self.hashlist[arrayIndex] = LinkedList()
        self.hashlist[arrayIndex].add(data)
        self.size += 1
        return True

    def search(self, data):
        hashcodeData = hash(data)
        arrayIndex = abs(hashcodeData) % self.hashsize
        if self.hashlist[arrayIndex]:
            return self.hashlist[arrayIndex].search(data)

    def len(self):
        return self.size


class HashTableSet:
    def __init__(self, hashsize=10000):
        self.set = HashTable(hashsize)

    def add(self, data):
        if not self.set.search(data):
            self.set.add(data)
            return True
        return False

    def contains(self, data):
        return self.set.search(data)

    def size(self):
        return self.set.len()


if __name__ == "__main__":
    HT = HashTable()
    HT.add('UCI')
    HT.search('UCI')