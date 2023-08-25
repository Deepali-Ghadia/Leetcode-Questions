from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)  # Convert to set to remove duplicates
        
        # since we need to find positive missing, therefore it is set to 1
        smallest_missing = 1
        while smallest_missing in nums:
            smallest_missing += 1
            
        return smallest_missing
    
    
nums = [int(x) for x in input().split()]

s1 = Solution()
print(s1.firstMissingPositive(nums))