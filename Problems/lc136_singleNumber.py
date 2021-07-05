class Solution(object):
    def singleNumber(self, nums):
        """
        Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

        You must implement a solution with a linear runtime complexity and use only constant extra space.

        Example 1:
        Input: nums = [2,2,1]
        Output: 1
        
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        for i in range(1, len(nums)):
            res ^= nums[i]
        return res
        
#print(Solution().singleNumber([2, 2, 1]))
print(Solution().singleNumber([4,1,2,1,2]))