
def sum(a: int, b: int) -> int:
    return a+b

print(sum(45, 1943))

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says woof!")

d = Dog("Willow")
d.bark()

 # NODE CLASS
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# LINKED LIST CLASS
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.tail is None and self.head is None:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def print_list(self):
        if self.tail is None and self.head is None:
            return None
        
        pnt = self.head
        res = []
        while pnt != None:
            res.append(pnt.data)
            pnt = pnt.next
        print(res)

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def delete(self, data):
        if self.head is None:
            return None
        
        prev = None
        curr = self.head
        
        while curr is not None:
            if data == curr.data:
                if prev is None:
                    self.head = self.head.next
                    break
                elif curr == self.tail:
                    self.tail = prev
                    prev.next = None
                    break
                else:
                    prev.next = curr.next
                    break

            prev = curr
            curr = curr.next


ll = LinkedList()
ll.append(20)
ll.append(-10)
ll.append(99)
ll.prepend(12)
ll.append(-123)

ll.delete(20)   # head
ll.print_list()

ll.delete(99)   # tail
ll.print_list()

ll.delete(-10)  # middle 

ll.print_list()

# STACK CLASS
class Stack:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def pop(self):
        if self.head is None:
            return None
        value = self.head.data
        self.head = self.head.next
        return value

s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())  
print(s.pop())  
print(s.pop())  
print(s.pop())  

# QUEUE CLASS
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
        # adds new element to queue
    def dequeue(self):
        # removes front element
        if self.head is None:
            return None
        value = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return value

    def peek(self):
        # returns first element
        if self.head is None:
            return None
        return self.head.data
    
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.dequeue())  # should be 10
print(q.peek())     # should be 20
print(q.dequeue())  # should be 20
print(q.dequeue())  # should be 30
print(q.dequeue())  # should be None

# HASH TABLE CLASS
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self._hash(key)

        if self.table[index] is None:
            self.table[index] = LinkedList()
        self.table[index].append((key, value))


            

    
    def get(self, key):
        index = self._hash(key)

        if self.table[index] is None:
            return None

        curr = self.table[index].head

        while curr is not None:
            if curr.data[0] == key:
                return curr.data[1]
            curr = curr.next

        return None


ht = HashTable()
ht.insert("name", "John")
ht.insert("age", 25)
ht.insert("city", "Boston")

print(ht.get("name"))  # John
print(ht.get("age"))   # 25
print(ht.get("city"))  # Boston
print(ht.get("missing"))  # None 
