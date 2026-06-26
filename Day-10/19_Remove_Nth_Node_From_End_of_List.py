# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return head.next
        curr = head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        count = 1
        while curr.next:
            curr = curr.next
            count+=1
            if count > n:
                prev = prev.next
        prev.next = prev.next.next
        return dummy.next