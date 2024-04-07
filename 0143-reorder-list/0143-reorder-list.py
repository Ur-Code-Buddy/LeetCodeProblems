# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        second = slow.next
        prev = slow.next = None
       
        
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
            
        #merge the two halfs
        
        first, second = head, prev
        
        while second:
            tem1, tem2 = first.next, second.next
            first.next = second
            second.next = tem1
            first,second = tem1,tem2
            
            
            
            