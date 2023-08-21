from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sorted_array = sorted(nums)
        
        missing_number = 0
        
        if n == 1:
            if sorted_array[0] == n:
                missing_number = 0
            else: missing_number = 1


        if sorted_array[-1] != n:
            missing_number = n

        else:
            for i in range(1, n):  # Start the loop from index 1
                if sorted_array[i] - sorted_array[i-1] != 1:
                    missing_number = sorted_array[i-1] + 1

        return missing_number



s = Solution()
nums = [int(x) for x in input().split()]
result = s.missingNumber(nums)
print(result)