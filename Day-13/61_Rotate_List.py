# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        n = len(nodes)
        k = k%n
        if k == 0: return nodes[0]

        parent = nodes[n-k-1]
        parent.next = None
        last = nodes[n-1]
        last.next = nodes[0]
        return nodes[n-k]