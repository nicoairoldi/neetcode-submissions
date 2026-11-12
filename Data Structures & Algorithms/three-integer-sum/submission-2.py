class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        sorted_list = sorted(nums)
        for i, num in enumerate(sorted_list):
            if num != sorted_list[i-1] or i==0:
                j = i + 1
                k = len(nums) - 1
                while j < k:
                    if k == (len(nums)-1) or sorted_list[k] != sorted_list[k+1]:
                        x = num + sorted_list[j] + sorted_list[k]
                        if x == 0:                                                     
                            output.append([num,sorted_list[j],sorted_list[k]])
                            j = j + 1
                            k = k - 1
                        if x < 0:
                            j = j + 1
                        if x > 0:
                            k = k -1
                    else: 
                        k = k -1
        return output



