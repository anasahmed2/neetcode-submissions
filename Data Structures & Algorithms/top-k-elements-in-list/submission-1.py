class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        my_dict = {}

        for num in nums:

            if num in my_dict:

                my_dict[num] += 1

            else:

                my_dict[num] = 1

        another_list = sorted(my_dict.items(), key=lambda pair: pair[1], reverse=True)

        new_list = []

        for num, freq in another_list[:k]:

            new_list.append(num)

        return new_list
