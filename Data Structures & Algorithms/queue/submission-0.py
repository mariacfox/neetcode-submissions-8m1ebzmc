class Node: # doubly linked list node
    def __init__(self, val):
        self.val = val
        self.next = self.prev = None


class Deque:
    
    def __init__(self):
        # two dummy nodes
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        new_node = Node(value)
        last_node = self.tail.prev # get node before tail

        # update all four pointers
        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self.tail
        self.tail.prev = new_node

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        # insert between dummy head and node after dummy
        first_node = self.head.next

        # update four pointers
        self.head.next = new_node
        new_node.prev = self.head
        new_node.next = first_node
        first_node.prev = new_node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        target_node = self.tail.prev # will always be real node
        value = target_node.val
        prev_node = target_node.prev

        prev_node.next = self.tail
        self.tail.prev = prev_node

        return value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        target_node = self.head.next
        value = target_node.val
        next_node = target_node.next

        self.head.next = next_node
        next_node.prev = self.head # becomes new head

        return value
        
