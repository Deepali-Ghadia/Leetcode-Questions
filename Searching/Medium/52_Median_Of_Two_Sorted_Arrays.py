from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_array = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                new_array.append(nums1[i])
                i += 1
            else:
                new_array.append(nums2[j])
                j += 1

        new_array.extend(nums1[i:])
        new_array.extend(nums2[j:])


        total_length = len(new_array)
        if total_length % 2 == 1:
            return new_array[total_length // 2]
        else:
            mid1 = new_array[total_length // 2 - 1]
            mid2 = new_array[total_length // 2]
            return (mid1 + mid2) / 2
        
        
        
nums1 = [int(x) for x in input().split()]

nums2 = [int(x) for x in input().split()]


s1 = Solution()
print(s1.findMedianSortedArrays(nums1, nums2))