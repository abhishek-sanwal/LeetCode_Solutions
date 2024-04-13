class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val) + "->" + str(self.next)


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    # 0(N)
    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        
        current = self.head
        for _ in range(index):
            current = current.next
        return current.val
    
    # 0(1)
    def addAtHead(self, val):
        node = ListNode(val)
        node.next = self.head
        self.head = node
        
        if self.size == 0:
            self.tail = node
        
        self.size += 1
    
    #0(1)
    def addAtTail(self, val):
        node = ListNode(val)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        
        self.size += 1

    #0(N)
    def addAtIndex(self, index, val):
        if index < 0 or index > self.size:
            return
        #
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            
            node = ListNode(val)
            node.next = current.next
            current.next = node
            
            self.size += 1
    #0(N)
    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        
        if index == 0:
            self.head = self.head.next
            if self.size == 1:
                self.tail = None
                #self.size -= 1
        else:
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next
            
            prev.next = prev.next.next
            if index == self.size - 1:
                self.tail = prev
        
        self.size -= 1
