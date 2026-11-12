class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        my_dict = {}

        for string in strs:

            key = ''.join(sorted(string))

            if key not in my_dict:

                my_dict[key] = []

            my_dict[key].append(string)

        return list(my_dict.values())

