# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head == None):
            return None
        current = head
        while current != None and current.next != None:
            temp = current.val
            current.val = current.next.val
            current.next.val = temp
            current = current.next.next
        return head