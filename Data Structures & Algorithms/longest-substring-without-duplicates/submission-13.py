class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        best = 0
        my_dict = {}

        for right in range(len(s)):

            if s[right] in my_dict and my_dict[s[right]] >= left:

                left = my_dict[s[right]] + 1

        
            my_dict[s[right]] = right
            best = max(best, right - left + 1)

        return best

            
        