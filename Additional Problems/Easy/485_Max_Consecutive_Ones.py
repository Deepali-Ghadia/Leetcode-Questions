from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        # converting into string and then using split function
        # converts a list of integers (nums) into a single string (nums_str). 
        nums_string = "".join(map(str, nums))

        substrings = nums_string.split("0")

        for item in substrings:
            if len(item) > max:
                max = len(item)

        return max