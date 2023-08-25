from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        min_len = min(len(item) for item in strs)
        
        prefix = ""
        
        for i in range(min_len):
            common_char = strs[0][i]
            
            if all(item[i] == common_char for item in strs):
                prefix += common_char
            else:
                break
        
        return prefix
    
    
strs = [x for x in input().split()]

s1 = Solution()
print(s1.longestCommonPrefix(strs))