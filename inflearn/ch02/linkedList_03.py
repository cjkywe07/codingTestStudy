# Linked List

class Node:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newNode

        self.length += 1
    
    def insert(self, idx, data):
        if 0 <= idx <= self.length:
            newNode = Node(data)

            curr = self.head
            for _ in range(idx - 1):
                curr = curr.next
            newNode.next = curr.next
            curr.next = newNode

            self.length += 1

    def remove(self, idx):
        if 0 <= idx <= self.length:
            curr = self.head
            for _ in range(idx - 1):
                curr = curr.next
            curr.next = curr.next.next

            self.length -= 1

    def get(self, idx):
        if 0 <= idx <= self.length:
            curr = self.head
            for _ in range(idx):
                curr = curr.next
            return curr.data
        
    def show(self):
        curr = self.head
        while curr:
            print(curr.data, end = " -> ")
            curr = curr.next
        print()

li = LinkedList()
li.append(1)
li.append(2)
li.append(3)
li.append(4)
li.append(5)
print(li.get(3))
li.insert(3, 11)
li.show()
li.remove(2)
li.show()
