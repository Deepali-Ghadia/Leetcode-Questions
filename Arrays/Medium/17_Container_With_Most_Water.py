from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = 0
        for i in range(len(height)):
            for j in range(i, len(height)):
                box_height = min(height[i], height[j])
                width = j-i
                if box_height * width > max:
                    max = box_height * width

        return max
    
height = [int(x) for x in input().split()]
s1 = Solution()
print(s1.maxArea(height))