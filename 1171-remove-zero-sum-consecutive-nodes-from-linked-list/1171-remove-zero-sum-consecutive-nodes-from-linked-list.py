# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeZeroSumSublists(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prefix = 0
        prefixToNode = {0: dummy}

        while head:
            prefix += head.val
            if prefix in prefixToNode:
                node = prefixToNode[prefix].next
                temp = prefix + node.val
                while temp != prefix:
                    del prefixToNode[temp]
                    node = node.next
                    temp += node.val
                prefixToNode[prefix].next = head.next
            else:
                prefixToNode[prefix] = head
            head = head.next

        return dummy.next
