# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 11:04:26 2024

@author: s22sethselv
"""

from doubly_linked_list import DoublyLinkedList

new_list = DoublyLinkedList()
print("new_list: ")
new_list.print_list()
new_list.insert_at_start(5)
new_list.insert_at_start(10)
new_list.insert_at_start(15)
print("new_list after inserting at the beginning: ")
new_list.print_list()


new_list = DoublyLinkedList()

new_list.insert_at_end(0)
new_list.insert_at_start(10)
new_list.print_list()
new_list.insert_at_start(20)
new_list.insert_at_start(30)
new_list.print_list()
new_list.insert_at_end(100)
new_list.insert_at_end(200)
new_list.print_list()