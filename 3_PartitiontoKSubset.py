#Partition to K Equal Sum Subsets - from Leetcode 698

class Solution:
	def canPartitionKSubsets(self, nums:list[int], k:int)->bool:
		if self.isDivisibleSubset(nums, k) == False:
			return False
		else:
			every_combinations = self.subset(nums, k)
			found = False
			for index in range(len(every_combinations)):
				sum_reference = sum(every_combinations[index][0])
				count = 1

				for i in range(1, len(every_combinations[index])):
					sum_target = sum(every_combinations[index][i])
					if sum_reference == sum_target:
						count += 1
				if count == len(every_combinations[index]):
					found = True
			return found

	def isDivisibleSubset(self, nums:list[int], k:int)->bool:
		if k > len(nums):
			return False
		else:
			return True

	def subset(self, nums:list[int], k:int)->list[int][int][int]:
		out_list: list[int][int][int]
		

