# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        runner = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                runner.next = l1
                l1 = l1.next
            else:
                runner.next = l2
                l2 = l2.next
            runner = runner.next
        if l1:
            runner.next = l1
        else:
            runner.next = l2
        return dummy.next
