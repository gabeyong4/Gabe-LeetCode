from typing import Optional

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
    
    # setters and getters
    def setValue(self, value) -> None:
        self.value = value
    
    def setNext(self, next) -> None:
        self.next = next
    
    def getValue(self) -> int:
        return self.value
    
    def getNext(self) -> Optional['Node']:
        return self.next
    
    def __str__(self) -> str:
        """Return a string representation of the Node."""
        return str(f"Node({self.value})")


class BasicLinkedList:
    def __init__(self, head) -> None:
        self.head = head

    def size(self):
        size = 1
        curr_node = self.head
        while curr_node.getNext() != None:
            size+=1
            curr_node = curr_node.getNext()
        return size
            
    def getItemAtIndex(self, index) -> int:
        curr_node = self.head
        curr_index = 0
        if index < 0 or index >= self.size():
            return "invalid index"
        while curr_index != index:
            curr_index += 1
            curr_node = curr_node.getNext()
        return curr_node.getValue()
    
    def insertItemAtIndex(self, item, index):
        print(f"Index: {index}")
        print(f"Size: {self.size()}")
        # create a new node
        new_node = Node(item)
        curr_node = self.head
        if (index < 0) or (index > self.size()):
            return "invalid index"
        for i in range(self.size()):
            if index == 0:
                old_head = self.head
                self.head = new_node
                self.head.setNext(old_head)
            elif i == index:
                replaced = curr_node.getNext()
                print(f'Replaced:{replaced}')
                curr_node.setNext(new_node)
                new_node.setNext(replaced)
            elif i == 0:
                curr_node = curr_node
            else:
                curr_node = curr_node.getNext()
        if index == self.size():
            curr_node.setNext(new_node)
    
    def removeNodeAtIndex(self, index):
        curr_node = self.head
        if index < 0 or index >= self.size():
            return "invalid index"
        for i in range(self.size()):
            if index == 0:
                new_head = curr_node.getNext()
                self.head = new_head
            elif i == index:
                curr_node.setNext(curr_node.getNext().getNext())
            elif i == 0:
                curr_node = curr_node
            else:
                curr_node = curr_node.getNext()

    def __str__(self) -> str:
        """Return a string representation of the Linked List."""
        return str(f"head of this linked list: {self.head}")


node_one = Node(1)
print(node_one)

node_two = Node(2)
print(node_two)

node_three = Node(3)
print(node_three)

node_one.setNext(node_three)
print(f'Node(1) neighbour: {node_one.getNext()}')
print(f'Node(3) neighbour: {node_three.getNext()}')

node_three.setNext(node_two)
print(f'Node(3) neighbour: {node_three.getNext()}')
print(f'Node(2) neighbour: {node_two.getNext()}')

basicLinkedlist = BasicLinkedList(node_one)
print(basicLinkedlist)

size = basicLinkedlist.size()
print(f'Size of the LL: {size}')

print(basicLinkedlist.getItemAtIndex(-1))
print(basicLinkedlist.getItemAtIndex(3))
print(basicLinkedlist.getItemAtIndex(1))

basicLinkedlist.insertItemAtIndex(4, 3)
print(f'Current head: {basicLinkedlist.head}')
print(f'Current: {basicLinkedlist.head.getNext()}')
print(f'Current: {basicLinkedlist.head.getNext().getNext()}')
print(f'Current: {basicLinkedlist.head.getNext().getNext().getNext()}')

basicLinkedlist.removeNodeAtIndex(3)
#print(basicLinkedlist.size())
print(f'Current head: {basicLinkedlist.head}')
print(f'Current: {basicLinkedlist.head.getNext()}')
print(f'Current: {basicLinkedlist.head.getNext().getNext()}')