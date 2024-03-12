# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # linked_array = []
        # current = head
        # while current:
        #     linked_array.append(current.val)
        #     current = current.next
        dummy = ListNode(0, head)
        prefix = 0
        prefixToNode = {0: dummy}

        while head:
          prefix += head.val
          prefixToNode[prefix] = head
          head = head.next

        prefix = 0
        head = dummy

        while head:
          prefix += head.val
          head.next = prefixToNode[prefix].next
          head = head.next

        return dummy.next