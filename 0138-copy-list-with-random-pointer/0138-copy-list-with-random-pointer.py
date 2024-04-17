"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None
        
        temp = head
        
        # Step 1 => Insert new copied node after each original node
        while temp:
            
            x = temp.next
            
            ne = Node(temp.val)
            temp.next = ne
            ne.next = x
            temp = x
            
        #  Step2 => Fill random pointers
        temp = head
        
        while temp:
            temp.next.random = temp.random.next if temp.random else None
            temp = temp.next.next
            
        # Steps 3 => Segregrate duplicate list
        temp = head.next
        
        while temp:
            
            temp.next = temp.next.next if temp.next else None
            temp = temp.next
            
        return head.next
            
        