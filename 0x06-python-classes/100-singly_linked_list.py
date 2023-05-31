#!/usr/bin/python3
"""
This module defines a Node & SinglyLinkedList Class
"""


class Node:
    """
    A Node class for a singly linke list
    """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    A SinglyLinkedList Class
    """

    def __init__(self):
        self.__head = None

    def __str__(self):
        string_value = ""
        head = self.__head

        if head is None:
            return string_value
        while head is not None:
            string_value += str(head.data)
            if head.next_node is not None:
                string_value += "\n"
            head = head.next_node
        return string_value

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position
        in the list (increasing order)
        """
        new_node = Node(value, None)

        # if list is empty or value less than head data
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head  # add node at start
            self.__head = new_node  # update head
            return
        # else traverse through the list
        curr = self.__head
        prev = None
        while curr.next_node is not None:
            prev = curr
            curr = curr.next_node
            if value >= prev.data and value <= curr.data:
                prev.next_node = new_node
                new_node.next_node = curr
                return
        # value larger than all list data, so add to the end
        curr.next_node = new_node
        new_node.next_node = None
        return
