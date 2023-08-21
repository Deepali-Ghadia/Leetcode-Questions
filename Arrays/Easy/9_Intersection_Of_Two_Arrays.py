from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
            count_nums1 = Counter(nums1)
            result = []

            # count the frequency of elements in nums1,
            for num in nums2:
                if num in count_nums1 and count_nums1[num] > 0:
                    result.append(num)
                    count_nums1[num] -= 1
            
            return result
        
        
nums1 = [int(x) for x in input().split()]
nums2 = [int(x) for x in input().split()]

s1 = Solution()
result = s1.intersect(nums1, nums2)
print(result)