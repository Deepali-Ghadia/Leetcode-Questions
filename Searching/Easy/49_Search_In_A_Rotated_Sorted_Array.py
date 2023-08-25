from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        for i in range(len(nums)):
            if nums[i] == target:
                return True

        return False
    
nums = [int(x) for x in input().split()]

target = int(input())

s1 = Solution()
print(s1.search(nums, target))