from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1  
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[count] = nums[i]
                count += 1
        
        return count 
    
    
nums = [int(x) for x in input().split()]

s1 = Solution()
result = s1.removeDuplicates(nums)
print(result)