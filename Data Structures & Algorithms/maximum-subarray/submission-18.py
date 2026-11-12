class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
           
        cur = best = nums[0]
        
        for x in nums[1:]:
            cur = max(x, cur + x)   # extend or restart
            best = max(best, cur)   # record the best seen
        return best