# First:
# Time: O(n^2)
# Space: O(n)
#
# Second:
# Time: O(nlgn)
# Space: O(n)
#
# Given an integer array nums, return the length of the longest strictly 
# increasing subsequence.
#
# A subsequence is a sequence that can be derived from an array by deleting some 
# or no elements without changing the order of the remaining elements. For example, 
# [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
#
# Input: [10,9,2,5,3,7,101,18]
# Output: 4

class Solution:
    def lengthOfLIS1(self, nums):
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    
        return max(dp)
    
    def lengthOfLIS2(self, nums):
        def binarySearch(nums, target):
            lo, hi = 0, len(nums)-1
            while(lo <= hi):
                mid = lo + (hi - lo)//2
                if nums[mid] < target:
                    lo = mid + 1
                elif target < nums[mid]:
                    hi = mid - 1
                else:
                    return mid
            return lo
        
        import bisect
        
        cur = []
        for target in nums:
#            idx = binarySearch(cur, target)
            idx = bisect.bisect_left(cur, target)
            if idx == len(cur):
                cur.append(target)
            else:
                cur[idx] = target
        return len(cur)
    
print(Solution().lengthOfLIS1([10,9,2,5,3,7,101,18]))
print(Solution().lengthOfLIS2([10,9,2,5,3,7,101,18]))
print(Solution().lengthOfLIS1([0,1,0,3,2,3]))
print(Solution().lengthOfLIS2([0,1,0,3,2,3]))