class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        empty_list = []
        for i in range(len(nums)):
            if nums[i] not in empty_list:
                empty_list.append(nums[i])
            else:
                return True
        
        return False
         