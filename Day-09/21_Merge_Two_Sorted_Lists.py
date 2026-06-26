class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedList = ListNode(0)
        curr = mergedList
        temp1, temp2 = list1, list2
        while temp1 and temp2:
            if temp1.val < temp2.val:
                curr.next = ListNode(temp1.val)
                temp1 = temp1.next
            else:
                curr.next = ListNode(temp2.val)
                temp2 = temp2.next
            curr = curr.next
        if temp1:
            curr.next = temp1
        else:
            curr.next = temp2
        return mergedList.next