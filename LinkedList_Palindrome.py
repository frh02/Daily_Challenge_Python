'''
Given the head of a singly linked list, return true if it is a palindrome.
'''
#solution:

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        stack =[]
        ispalin = None 
        while slow!= None:
            stack.append(slow.val)
            slow = slow.next
        while head!= None:
            i = stack.pop()
            if head.val== i:
                ispalin = True
            else:
                ispalin = False
                break 
            head= head.next
        return ispalin
            
