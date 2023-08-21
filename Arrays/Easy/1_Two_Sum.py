# Rules for specifying input
# First line contains array of integers: enter integer values separated by spaces
# Second line contains a integer specifying the target value
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
                    break
                j = j+1
            i = i+1

        return result
    

nums = [int(x) for x in input().split()]
target = int(input())

s1 = Solution()
result = s1.twoSum(nums, target)
print(result)