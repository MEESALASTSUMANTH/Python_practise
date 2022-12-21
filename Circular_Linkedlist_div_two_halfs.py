# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 21:17:14 2022

@author: suman
"""

#SPLITTING THE CIRCULAR LINKED LIST INTO TWO HALVES
class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
        
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def printList(self):
        temp = self.head
        if self.head is not None:
            while(True):
                print (temp.data,end=' ')
                temp = temp.next
                if (temp == self.head):
                    break 
    def push(self, data):
        ptr1 = Node(data)
        temp = self.head
        ptr1.next = self.head
        if self.head is not None:
            while(temp.next != self.head):
                temp = temp.next 
            temp.next = ptr1
  
        else:
            ptr1.next = ptr1 
  
        self.head = ptr1 
        
    def split_Clinkedlist(self,head1,head2):
        slowptr = self.head 
        fastptr = self.head
        
        while(fastptr.next!= self.head and fastptr.next.next != self.head):
            fastptr = fastptr.next.next
            slowptr = slowptr.next 
            
        if (fastptr.next.next == self.head):
            fastptr = fastptr.next 
            
        head1.head = self.head 
        
        if self.head.next !=self.head:
            head2.head = slowptr.next
            
        fastptr.next = slowptr.next 
        slowptr.next = self.head 
        

head = Linkedlist()
head1 = Linkedlist()
head2 = Linkedlist()
  
head.push(14)
head.push(56)
head.push(2)
head.push(11)
head.push(19)
head.push(29)
head.printList()
head.split_Clinkedlist(head1 , head2)
print("\nthe values in head1:",end= " ")
head1.printList()
print("\nthe values in head2:",end =" ")
head2.printList()


        
        
    