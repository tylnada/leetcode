"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# genius solution
class Solution:
    def copyRandomList(self, head):
        
        if not head: return 
        
        old = head
		
        # copy node values
        while old:
            new = Node(old.val)
            old.copy = new #
            old = old.next
        
        # reset for 2nd loop
        old = head

        #copy node relationships
        while old:
            new = old.copy
            new.next = old.next.copy if old.next else None
            new.random = old.random.copy if old.random else None
            old = old.next
            
        return head.copy
