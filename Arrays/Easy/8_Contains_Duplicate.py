from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sorted_array = sorted(nums)

        for i in range(1, len(sorted_array)):
            if sorted_array[i-1] == sorted_array[i]:
                return True

        return False
    

nums = [int(x) for x in input().split()]
s1 = Solution()
result = s1.containsDuplicate(nums)
print(result)