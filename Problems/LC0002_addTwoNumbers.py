# Time:  O(n)
# Space: O(1)
#
# You are given two linked lists representing two non-negative numbers. 
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        root = n = ListNode(0)
        
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
                
            carry, val = divmod(v1+v2+carry, 10)
            n.next = ListNode(val)
            n = n.next
            
        return root.next
    
a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(4)
result = Solution().addTwoNumbers(a, b)
print("{0} -> {1} -> {2}".format(result.val, result.next.val, result.next.next.val))