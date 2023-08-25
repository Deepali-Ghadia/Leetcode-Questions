class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # using set to keep track of characters in the window
        window = set()

        left = 0
        result = 0


        for i in range(len(s)):
            # if the character is in the charset and again found while traversing => it is repeated, 
            while s[i] in window:
                window.remove(s[left])
                left = left + 1

            window.add(s[i])
            result = max(result, i - left + 1)

        return result


s = input()
s1 = Solution()
print(s1.lengthOfLongestSubstring(s))
# window = set(): This initializes an empty set called window. The set is used to keep track of the characters within the current window of the substring being considered.

# left = 0: This initializes the left pointer, which marks the left boundary of the current window.

# result = 0: This initializes the result variable to keep track of the length of the longest substring without repeating characters found so far.

# The for loop iterates through each character in the string s.

# Inside the loop, the while loop checks if the current character s[i] is already in the window set. If it is, this means that the character is repeated, and we need to remove the leftmost character from the window (by incrementing left) until there are no repetitions in the window.

# After ensuring no repetitions, the current character s[i] is added to the window set.

# The length of the current substring (without repeating characters) is given by i - left + 1.

# The result is updated with the maximum value between the current result and the length of the current substring.

# Finally, after the loop, the result variable holds the length of the longest substring without repeating characters, which is returned as the output of the method.