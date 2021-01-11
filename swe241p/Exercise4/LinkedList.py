#!/usr/bin/env python
# coding: utf-8
# University of California, Irvine
# Master of Software Engineering, Donald Bren School of Information and Computer Science
# Created by: Xinyi Hu
# Date      : 2020/10/11
# Contact   : xinyih20@uci.edu
# Target    : Realize Linked List by scratch in Python
# Reference : The algorithm design manual


class Node:
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.next = nextNode


class LinkedList:
    def __init__(self):
        self.head = None

    #     def data(self):
    #         current = self.head
    #         if current.data:
    #             return current.data
    #         return None

    #     def next(self):
    #         if self.head.next:
    #             self.head = self.head.next
    #         self.head = Node()

    def add(self, data):
        if data is None:
            return None

        node = Node(data)
        if self.head is None:
            self.head = node
            return node

        current = self.head
        while current.next:
            current = current.next
        current.next = node
        return node

    def len(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def print(self):
        current = self.head
        while current and current.next:
            print(current.data, end=' -> ')
            current = current.next
        print(current.data)
        return
    
    def print_alpha(self):
        current = self.head
        while current and current.next:
            print(chr(current.data+65), end=' -> ')
            current = current.next
        print(chr(current.data+65))
        return

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def delete(self, data):
        current = self.head
        if current.data == data:
            self.head = current.next
            return
        while current and current.next:
            if current.next.data == data:
                current.next = current.next.next
            current = current.next
        return