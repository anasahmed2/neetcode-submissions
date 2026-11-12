class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        best = 0
        left = 0
        last_seen = {}

        for r in range(len(s)):
            if s[r] in last_seen and last_seen[s[r]] >= left:
                left = last_seen[s[r]] + 1   

            last_seen[s[r]] = r
            best = max(best, r - left + 1)

        return best
        