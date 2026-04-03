class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head # dummy tail
    
    def get(self, index: int) -> int:
        curr = self.head.next  # Start at first real node
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1  # If we exit loop without finding index

    def insertHead(self, val: int) -> None:
        head = self.head
        first = head.next
        new_node = ListNode(val)
        new_node.next = first
        head.next = new_node
        if first is None:
            self.tail = new_node


    def insertTail(self, val: int) -> None:
        tail = self.tail
        new = ListNode(val)
        tail.next = new
        self.tail = new


    def remove(self, index: int) -> bool:
        head = self.head
        i = 0
        while i < index and head:
            head = head.next
            i += 1

        if head and head.next:
            if head.next == self.tail:
                self.tail = head
            head.next = head.next.next
            return True
        else:
            return False

        

    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res

# this was a slog. needed lots of help working through this one.