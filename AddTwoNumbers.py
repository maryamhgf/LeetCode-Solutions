# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head1 = l1
        head2 = l2
        remainder = 0
        head = None
        prev_node = None
        while(head1 != None or head2 != None):
            sum = head1.val + head2.val + remainder
            digit = sum % 10
            remainder = int(sum/10)
            new_node = ListNode(val=digit, next=None)
            if(prev_node == None):
                head = new_node
            else:
                prev_node.next = new_node
            head1 = head1.next
            head2 = head2.next
            prev_node = new_node
            if(head1 == None and head2 == None):
                break
            if(head1 == None):
                head1 = ListNode(val=0, next=None)
            if(head2 == None):
                head2 = ListNode(val=0, next=None)
        if(remainder != 0):
            new_node = ListNode(val=remainder, next=None)
            prev_node.next = new_node
        return(head)