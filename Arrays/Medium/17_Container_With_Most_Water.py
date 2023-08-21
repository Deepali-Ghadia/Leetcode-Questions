from typing import List

# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         max = 0
#         for i in range(len(height)):
#             for j in range(i, len(height)):
#                 box_height = min(height[i], height[j])
#                 width = j-i
#                 if box_height * width > max:
#                     max = box_height * width

#         return max
    
    
    
# optimised solution
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1
        
        while left < right:
            min_height = min(height[left], height[right])
            width = right - left
            area = min_height * width
            max_area = max(max_area, area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
    
    
height = [int(x) for x in input().split()]
s1 = Solution()
print(s1.maxArea(height))