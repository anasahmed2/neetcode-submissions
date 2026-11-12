class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_area = 0

        left = 0

        right = len(heights) - 1
        

        while left < right:

            curr_height = min(heights[left], heights[right])

            curr_length = right - left

            curr_area = curr_length * curr_height

            if curr_area > max_area:

                max_area = curr_area

            if heights[left] < heights[right]:
                left += 1
            else:

                right -= 1

        return max_area