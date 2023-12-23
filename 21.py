# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l1=list1
        l2=list2
        dummy_head=ListNode(0)
        dummy_head.next=l1
        pre_l1=dummy_head
        while l1 is not None and l2 is not None:
            if l2.val<l1.val:
                temp2=l2.next
                l2.next=l1 
                pre_l1.next=l2 
                l2=temp2 
                pre_l1=pre_l1.next
            else:
                l1=l1.next
                pre_l1=pre_l1.next
        if l1 is not None:
            pass
        if l2 is not None:
            pre_l1.next=l2
        return dummy_head.next