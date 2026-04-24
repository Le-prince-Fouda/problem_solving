# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # create an initial linkedlist as starting ponit
        myLinkedList = ListNode(0)
        current = myLinkedList
        carry = 0

        # Continue as long as there is a node in l1, l2 OR a remaining carry
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate sum and carry
            add = val1 + val2 + carry
            carry = add//10
            # Create a new node with the digit part of the sum
            current.next = ListNode(add%10)

            # Move forward in the result list and input lists
            current = current.next
            if l1: l1 =l1.next
            if l2: l2 = l2.next
        return myLinkedList.next

