# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        ptr1 = head
        ptr2 = head
        if(head.next == None and n != 0):
            return head.next
        for _ in range(n):
            ptr2 = ptr2.next
        if(ptr2 == None):
            return ptr1.next
        while ptr2:
            ptr2 = ptr2.next
            if(ptr2 == None):
                break
            ptr1 = ptr1.next
        if(ptr1.next != None):
            ptr1.next = ptr1.next.next
        return head