from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j=0
        for i in nums:
            if i!=0:
                nums[j]=i
                j+=1               
        while(j<len(nums)):
            nums[j]=0
            j+=1
            
        print(nums)
            
nums = [int(x) for x in input().split()]


s1 = Solution()
s1.moveZeroes(nums)
