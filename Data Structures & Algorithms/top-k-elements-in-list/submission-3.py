class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        my_dict = {}

        for num in nums:

            if num not in my_dict:

                my_dict[num] = 0

            my_dict[num] += 1

        sorted_list = sorted(my_dict.items(), key=lambda pair: pair[1], reverse=True)

        empty_list = []

        for num, count in sorted_list[:k]:

            empty_list.append(num)

        return empty_list
