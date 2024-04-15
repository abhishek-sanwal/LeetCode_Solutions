
class ListNode:
    
    def __init__(self,val, key , prev = None, nextt = None):
        
        self.val = val
        self.prev = prev
        self.next = nextt
        self.key = key
        
class DoublyLinkedList:
    
    def __init__(self):
        
        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    # 0(1)
    def delete_last_element(self):
        
        node = self.tail.prev
        
        node.prev.next = self.tail
        self.tail.prev = node.prev
        
        return node
        
    
    #0(1)
    def insertAfterHead(self,val,key):
        
        newNode = ListNode(val,key)
        
        if self.head.next == self.tail:
            #print("true","empty")
            
            self.head.next = newNode
            newNode.prev = self.head
            newNode.next = self.tail
            self.tail.prev = newNode
            return newNode
        
        temp = self.head
        
        # After node
        x = temp.next
        
        temp.next = newNode
        newNode.prev = temp
        newNode.next = x
        x.prev = newNode
        return newNode
    
    # 0(1) time
    def deleteNode(self,node):
        
        x = node.prev
        y = node.next
        x.next = y
        y.prev = x
        
        return
            
class LRUCache(object):
    
    
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        
        self.mapp = dict()
        self.dl = DoublyLinkedList()
        self.size = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        #self.dl.printList()
        
        if key not in self.mapp:
            return -1
        
        node = self.mapp[key]
        
        x = node.val
        
        # Delete Node
        #0(1)
        self.dl.deleteNode(node)
        
        # Insert node with same value
        # 0(1)
        self.mapp[key] = self.dl.insertAfterHead(x,key)
        return x
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.mapp:

            # Delete Node
            self.dl.deleteNode(self.mapp[key])
            #0(1)
        
        elif len(self.mapp) == self.size:
            #0(1)
            x = self.dl.delete_last_element()
            del self.mapp[x.key]
            del x
            
        #0(1)
        self.mapp[key] =  self.dl.insertAfterHead(value,key)
        #print(self.dl.printList())
        #print(self.mapp)
        return None
        
            
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)