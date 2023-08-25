from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < minimum:
                minimum = nums[i]

        return minimum
    
nums = [int(x) for x in input().split()]

s1 = Solution()
print(s1.findMin(nums))