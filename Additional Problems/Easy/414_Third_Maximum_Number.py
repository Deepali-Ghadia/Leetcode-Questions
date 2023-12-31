from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        first = second = third = float('-inf')  # Initialize with negative infinity
    
        for num in nums:
            if num > first:
                third = second
                second = first
                first = num
            elif num > second and num < first:
                third = second
                second = num
            elif num > third and num < second:
                third = num
                
        if third != float('-inf'):
            return third
        else:
            return first