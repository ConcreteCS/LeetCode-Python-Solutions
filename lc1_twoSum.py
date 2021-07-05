# Time:  O(n)
# Space: O(n)

# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution(object):
    def twoSum(self, nums, target):
        rem = dict()
        
        for i, num in enumerate(nums):
            if nums[i] in rem:
                return [i, rem[nums[i]]]
            else:
                rem[target - nums[i]] = i
            
#print(Solution().twoSum([2,7,11,15], 9))
#print(Solution().twoSum([3,2,4], 6))
#print(Solution().twoSum([3,3], 6))