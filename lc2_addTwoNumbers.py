class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        root = n = ListNode(0)
        
        while l1 or l2 or carry:
            print("l1:", l1, "l2:", l2, "carry:", carry)
            
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
                
            carry, val = divmod(v1+v2+carry, 10)
            print("carry:", carry, "val:", val)
            
            n.next = ListNode(val)
            print("n:", n)
            
            n = n.next
            
            print("\n")
            
        return root.next
    
a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(4)
result = Solution().addTwoNumbers(a, b)
print("{0} -> {1} -> {2}".format(result.val, result.next.val, result.next.next.val))