from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = ""
        
        for i in range(len(digits)):
            number += str(digits[i])

        incremented = int(number) + 1
        
        # converting back to list
        result = [int(x) for x in str(incremented)]

        return result