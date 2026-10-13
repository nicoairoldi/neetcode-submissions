class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest_sequence = 0
        cur_sequence = 0
        for num in s:
            if (num -1) not in s:
                cur_sequence = 0
                j = num
                while(j in s):
                    cur_sequence += 1
                    j += 1
                longest_sequence = max(longest_sequence, cur_sequence)
        return longest_sequence
