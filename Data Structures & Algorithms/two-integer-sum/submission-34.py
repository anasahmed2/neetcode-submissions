class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        my_set = {}
        
        for i in range(len(nums)):

            complement = target - nums[i]

            if complement in my_set:

                return [my_set[complement], i]
            
            my_set[nums[i]] = i


        return []


        