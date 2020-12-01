#Number of Good Pairs - from Leetcode 1512

#Runtime: +35.9%
#Memory Usage: -12.01%

class Solution:
	def numIdenticalPairs(self, nums:list[int])->int:
		count = 0
		for i in range(len(nums)):
			for j in range(i+1, len(nums)):
				if nums[i] == nums[j]:
					count += 1
		return count
