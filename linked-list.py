# Implement a linked list in Python

class Node:
    def __init__(self, data, ref=None):
        self.data = data
        self.ref = ref

class linkedList:
    def __init__(self):
        self.head = None
    
    def printList(self):
        if self.head is None:
            print("List is empty")
            return
        else:
            n = self.head
            while n is not None:
                print(n.data, " ")
                n = n.ref
    
    def addBegin(self, data):
        node = Node(data)
        node.ref = self.head
        self.head = node
        
    def addEnd(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        n = self.head
        while n.ref is not None:
            n = n.ref
        n.ref = node
        
    def addAfter(self, data, x):
        node = Node(data)
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("Node is not present in the list")
        else:
            node.ref = n.ref
            n.ref = node
    
    def addBefore(self, data, x):
        node = Node(data)
        if self.head is None:
            print("List is empty")
            return
        if x == self.head.data:
            node.ref = self.head
            self.head = node
            return
        n = self.head
        while n.ref is not None:
            if x == n.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not present in the list")
        else:
            node.ref = n.ref
            n.ref = node
            
    def remove(self, x):
        if self.head is None:
            print("List is empty")
            return
        if x == self.head.data:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if x == n.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not present in the list")
        else:
            n.ref = n.ref.ref
            
    def reverse(self):
        prev = None
        n = self.head
        while n is not None:
            next = n.ref
            n.ref = prev
            prev = n
            n = next
        self.head = prev
        
    def removeDuplicates(self):
        n = self.head
        while n is not None:
            if n.ref is not None and n.data == n.ref.data:
                n.ref = n.ref.ref
            else:
                n = n.ref
                
    def countNodes(self):
        n = self.head
        count = 0
        while n is not None:
            count += 1
            n = n.ref
        return count
    
    
        
        
        
        
            
            
        
            
        
    
            
    