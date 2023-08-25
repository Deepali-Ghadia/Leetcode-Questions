class Solution:
    def isValid(self, s: str) -> bool:
        # if open brackets -> add to stack
        # if close bracket -> pop the corresponding opeen bracket 
        # {{()}}
        stack = []
        # {{(
        mappings = {"(": ")", "{":"}", "[": "]"}

        for i in range(len(s)):
            if s[i] in "({[":
                stack.append(s[i])
            elif s[i] in ")}]" and stack and mappings[stack[-1]] == s[i]:
                stack.pop()
            else:
                return False

        return len(stack) == 0
    
    
s = input()

s1 = Solution()
print(s1.isValid(s))