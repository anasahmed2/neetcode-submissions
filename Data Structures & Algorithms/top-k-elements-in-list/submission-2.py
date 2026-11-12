class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        my_dict = {}

        for num in nums:

            if num not in my_dict:

                my_dict[num] = 1

            my_dict[num] += 1

        sorted_list = sorted(my_dict.items(), key= lambda pair: pair[1], reverse=True)

        new_list = []

        for num, count in sorted_list[:k]:

            new_list.append(num)

        return new_list
