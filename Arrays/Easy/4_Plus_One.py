from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # if len-> 6 then last index will be 5
        # will include till index 0 and last -1 is for reverse traversing
        
            if digits[-1] != 9:
                digits[-1] += 1
                return digits
            
            else:
                digits[-1] = 0
                new_digits = digits[:-1]
                if len(new_digits) > 0:
                    new_digits_result = self.plusOne(new_digits)  
                    return new_digits_result + [0]  # Append [0] to the end
                else:
                    return [1] + digits
                    

s = Solution()
input_digits = [int(x) for x in input().split()]
result = s.plusOne(input_digits)
print(result)