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
        if not head: return head
        obj = {}
        curr = head
        while curr:
            obj[curr] = Node(curr.val)
            curr = curr.next
        newList = Node(-1)
        curr = head
        while curr:
            obj[curr].next = obj.get(curr.next, None)
            obj[curr].random  = obj.get(curr.random, None)
            curr = curr.next
        return obj[head]