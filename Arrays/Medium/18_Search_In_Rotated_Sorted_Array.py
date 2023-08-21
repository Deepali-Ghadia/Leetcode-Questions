from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i

        return -1
    
    
nums = [int(x) for x in input().split()]
target = int(input())

s1 = Solution()
print(s1.search(nums, target))
