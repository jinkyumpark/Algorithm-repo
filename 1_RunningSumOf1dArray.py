#Running Sum of 1d Array - from LeetCode 1480

#Runtime: -81.41%, 36ms
#Memory Usage: -12.46%, 14.4MB

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_num = 0
        out_nums = []
        for i in range(len(nums)):
            sum_num += nums[i]
            out_nums.append(sum_num)
        return out_nums
