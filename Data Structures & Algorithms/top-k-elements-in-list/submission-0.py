class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        my_dict = {}

        for num in nums:
            if num in my_dict:
                my_dict[num] += 1

            else:
                my_dict[num] = 1

        max_list = sorted(my_dict.items(), key=lambda pair: pair[1], reverse = True)

        new_list = []

        for num, count in max_list[:k]:

            new_list.append(num)

        return new_list
