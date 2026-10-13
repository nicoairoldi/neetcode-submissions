class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest_sequence = 0
        cur_sequence = 0
        for i in range(len(nums)):
            if (nums[i] -1) not in s:
                cur_sequence = 0
                j = nums[i]
                while(j in s):
                    cur_sequence += 1
                    j += 1
                if cur_sequence > longest_sequence:
                    longest_sequence = cur_sequence
        return longest_sequence
