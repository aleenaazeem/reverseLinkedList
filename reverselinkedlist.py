class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
class linkedlist:
    def __init__(self):
        self.head = None #empty linkedlist
    def insert(self,data):
        new_node = Node(data)
        new_node.ref = self.head 
        self.head = new_node
    def reverse(self): 
        previous = None  #previous is null
        current  = self.head #current is the head of the list
        while current: 
            next = current.ref #next is adjacent to head
            current.ref = previous #Previous becomes adjacent to head 
            previous = current #previous becomes current
            current = next #current becomes next 
        self.head = previous
        return previous




LL1 = linkedlist()
LL1.insert(2)
LL1.insert(3)
LL1.insert(4)
LL1.reverse()
