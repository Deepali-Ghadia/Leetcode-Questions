from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0, len(nums)):
            product = 1
            for j in range(0, len(nums)):
                if i != j:
                    product = product * nums[j]

            result.append(product)

        return result
    
nums = [int(x) for x in input().split()]
s1 = Solution()
print(s1.productExceptSelf(nums))