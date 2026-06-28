class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        temp = head
        prev = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            temp.next = prev
            prev = temp
            temp = slow
        if fast:
            slow = slow.next
        while prev and slow:
            if prev.val != slow.val:
                return False
            prev = prev.next
            slow = slow.next
        return  True