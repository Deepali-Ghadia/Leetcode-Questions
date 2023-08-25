from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = (low+high)//2

            if target == nums[mid]:
                return mid

            elif target> nums[mid]:
                low = mid + 1  
            else:
                high = mid-1

        return low
        
        
nums = [int(x) for x in input().split()]

target = int(input())

s1 = Solution()
print(s1.searchInsert(nums, target))