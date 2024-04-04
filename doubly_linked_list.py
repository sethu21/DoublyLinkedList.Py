# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 11:02:25 2024

@author: s22sethselv
"""
class DoublyNode:
    
    def __init__(self,data):
        
        self.data = data
        self.next = None
        self.previous = None
        

class DoublyLinkedList:
    
    def __init__(self):
        
        self.head = None
        
    def print_list(self):
        
        if self.head is not None:
            
            current = self.head
            while current is not None:
                print(current.data, end=" ")
                current = current.next
            print()
        else:
            
            print("list has no element")
            
    def insert_at_start(self, data):
        
        new_node = DoublyNode(data)
        
        if self.head is None:
            
            self.head = new_node
        
        else:
            
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
            
    def insert_at_end(self, data):
        
        new_node = DoublyNode(data)
        
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
                
            current.next = new_node
            
            new_node.previous = current
            
    def insert_after_item(self, item, data):
        
        if self.head is not None:
            current = self.head
            while current is not none:
                if current.data !=item:
                    current = current.next
                else:
                    new_node = DoublyNode(data)
                    new_node.previous = current
                    new_node.next = current.next
                    if current.next is not None:
                        current.next.previous = new_node
                    current.next = new_node
                    break
            if current is None:
                print("item not in the list")
        else:
            print("list is empty")
            
            
            
            
            