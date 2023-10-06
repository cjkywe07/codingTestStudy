# Linked List(2)

class Node:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def insert_back(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = self.tail.next

        self.len += 1
    
    def insert_at(self, idx, data):
        newNode = Node(data)

        if idx == 0:
            newNode.next = self.head
            self.head = newNode
        elif idx > 0 and idx <= self.len:
            curr = self.head
            for _ in range(idx - 1):
                curr = curr.next
            newNode.next = curr.next
            curr.next = newNode

        self.len += 1

    def remove_back(self):
        if self.head is not None:
            curr = self.head
            last_idx = self.len - 1

            for _ in range(last_idx - 1):
                curr = curr.next
            curr.next = curr.next.next # 즉 None

            self.tail = curr.next
            self.len -= 1

    def remove_at(self, idx):
        if self.head is not None:
            if idx == 0:
                self.head = self.head.next
            elif idx > 0 and idx < self.len:
                curr = self.head
                for _ in range(idx - 1):
                    curr = curr.next
                curr.next = curr.next.next

            self.len -= 1

    def get(self, idx):
        if idx >= 0 and idx < self.len:
            curr = self.head
            for _ in range(idx):
                curr = curr.next
            return curr.data
        
    def show(self):
        curr = self.head
        while curr:
            print(curr.data, end = "")
            curr = curr.next
            if curr:
                print(" -> ", end = "")
        print()

li = LinkedList()

li.insert_back(1)
li.insert_back(2)
li.insert_back(3)
li.insert_back(4)
li.insert_back(5)
li.insert_back(6)
li.insert_back(7)
li.show()
print('len :', li.len)
print('li[3] :', li.get(3))
print('------------------------------')

li.remove_back()
li.show()
li.remove_back()
li.show()
print('len :', li.len)
print('------------------------------')

li.insert_at(0, 11)
li.insert_at(6, 12)
li.show()
print('len :', li.len)
print('------------------------------')

li.remove_at(0)
li.show()
li.remove_at(5)
li.show()
print('len :', li.len)
print('------------------------------')
