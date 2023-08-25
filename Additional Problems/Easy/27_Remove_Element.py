from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k = 0 # to keep track of count of non val elements

        for i in nums:
            if i != val:
                nums[k] = i
                k += 1
                print(nums)
        return k

