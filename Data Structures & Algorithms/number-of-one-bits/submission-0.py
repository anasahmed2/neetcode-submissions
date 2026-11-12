class Solution:
    def hammingWeight(self, n: int) -> int:

        bin_number = bin(n)[2:]

        count = str(bin_number).count('1')

        return count