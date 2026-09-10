class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (len(nums)* 2)
        cpy = len(nums)
        for i, val in enumerate(nums):
            ans[i] = nums[i]
            ans[cpy + i] = nums[i]
        return ans