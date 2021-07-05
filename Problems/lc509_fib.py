class Solution(object):
    
    def __init__(self):
        self.memo = {}
    
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)
        
    def fib2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        else:
            if n-1 not in self.memo:
                self.memo[n-1] = self.fib2(n-1)
            if n-2 not in self.memo:
                self.memo[n-2] = self.fib2(n-2)
            self.memo[n] = self.memo[n-1] + self.memo[n-2]
            return self.memo[n-1] + self.memo[n-2]
        
    def __str__(self):
        return(str(self.memo))
        
s = Solution()
print(s.fib2(20))
print(s)
