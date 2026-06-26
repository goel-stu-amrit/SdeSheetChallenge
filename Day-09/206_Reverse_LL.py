class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = None
        temp = head
        while temp:
            next1 = temp.next
            temp.next = prev
            prev = temp
            temp = next1
        return prev