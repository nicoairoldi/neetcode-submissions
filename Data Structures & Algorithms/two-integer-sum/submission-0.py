class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            if (target - num) in d:
                val = d[target - num]
                return [val, i]
            else:
                d[num] = i      