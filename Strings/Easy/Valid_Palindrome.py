class Solution:
    def isPalindrome(self, s: str) -> bool:

        new_string = ""
        charset = "abcdefghijklmnopqrstuvwxyz1234567890"

        # converting upper to lower
        s = s.lower()

        # removing non aphanumeric characters
        for i in range(len(s)):
            if s[i] in charset:
                new_string += s[i]

        if new_string == new_string[::-1]:
            return True
        else: 
            return False



s = input()

s1  =Solution()
print(s1.isPalindrome(s))