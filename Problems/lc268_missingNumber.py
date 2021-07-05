class Solution(object):
    def missingNumber1(self, nums):
        """
        Input: nums = [9,6,4,2,3,5,7,0,1]
        Output: 8
        Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
        
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        
        for num in range(len(nums)+1):
            res ^= num
        for elem in nums:
            res ^= elem
        
        return res
    
    def missingNumber2(self, nums):
        """
        Input: nums = [9,6,4,2,3,5,7,0,1]
        Output: 8
        Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
        
        :type nums: List[int]
        :rtype: int
        """
        desired_sum = (len(nums)+1)*(len(nums))/2
        cur_sum = sum(nums)
        res = int(desired_sum - cur_sum)
        
        return res
    
print(Solution().missingNumber1([9,6,4,2,3,5,7,0,1]))
print(Solution().missingNumber2([9,6,4,2,3,5,7,0,1]))