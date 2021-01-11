#!/usr/bin/env python
# coding: utf-8
# University of California, Irvine
# Master of Software Engineering, Donald Bren School of Information and Computer Science
# Created by: Xinyi Hu
# Date      : 2020/10/07
# Contact   : xinyih20@uci.edu
# Target    : Realize Binary Tree by scratch in Python
# Reference : The algorithm design manual


class BTNode:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data


class BinaryTree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, data):
        if self.root is None:
            self.root = BTNode(data)
        else:
            self.addByBinarySearch(data, self.root)

    def addByBinarySearch(self, data, node):
        if (data) < (node.data):
            if node.left:
                self.addByBinarySearch(data, node.left)
            else:
                node.left = BTNode(data)
        else:
            if node.right:
                self.addByBinarySearch(data, node.right)
            else:
                node.right = BTNode(data)

    def search(self, data):
        if self.root is None:
            return False
        return self.searchNode(data, self.root)

    def searchNode(self, data, node):
        if node.data == data:
            return True
        elif node.data < data and node.right is not None:
            return self.searchNode(data, node.right)
        elif node.data > data and node.left is not None:
            return self.searchNode(data, node.left)
        else:
            return False

    def print(self):
        self.printNode(self.root)

    def printNode(self, node):
        if node:
            if node.left:
                self.printNode(node.left)
            print(node.data, end=" ")
            if node.right:
                self.printNode(node.right)

    def len(self):
        if self.root:
            return self.lenNode(self.root)

    def lenNode(self, node):
        count = 0
        if node:
            count += 1
        if node.left:
            count += self.lenNode(node.left)
        if node.right:
            count += self.lenNode(node.right)
        return count


class BinaryTreeSet:
    def __init__(self):
        self.set = BinaryTree()

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
    BT = BinaryTree()
    print(BT.search(1))
    BT.add(1)
    BT.add(0)
    BT.add(2)
    print(BT.search(3))
    BT.add(3)
    print(BT.search(3))
    BT.add(4)
    BT.print()
    BT.add()