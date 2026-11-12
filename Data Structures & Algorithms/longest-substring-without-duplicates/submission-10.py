class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()
        max_length = 0
        left = 0

        for right in range(len(s)):

            while s[right] in seen:

                seen.remove(s[left])

                left += 1

            seen.add(s[right])

            current_length = right - left + 1

            if current_length > max_length:

                max_length = current_length

        return max_length
        