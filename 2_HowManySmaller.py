#How many numbers are smaller than the current number

#Runtime: +30.56%
#Memory Usage: -13.84%

class Solution:
	def smallerNumbersThanCurrent(self, nums:list[int])->list[int]:
		out_list = []
		for i1 in nums:
			count = 0
			for i2 in nums:
				if i1 != i2 and i2 < i1:
					count += 1
			out_list.append(count)
		return out_list
