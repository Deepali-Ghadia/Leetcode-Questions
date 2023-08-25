class Solution:
    def firstUniqChar(self, s: str) -> int:
        # using dictionary to track count of occurence of each character

        count = {}

        for char in s:
            if char not in count:
                count[char] = 1

            else:
                count[char] += count[char]
        

        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
            
        return -1
    
    
s = input()

s1 = Solution()
print(s1.firstUniqChar(s))