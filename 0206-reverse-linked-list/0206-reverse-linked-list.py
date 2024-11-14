# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current  = head
        previous_p = None

        while current:
            next_p = current.next
            current.next = previous_p
            previous_p = current
            current = next_p 
        return previous_p

        