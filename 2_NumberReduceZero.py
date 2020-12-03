#Number of steps to reduce a number to zero - from Leetcode 1342

#Runtime: +48.22%
#Memory Usage: -8.63%

class Solution:
	def numberOfSteps(self, num: int)->int:
		count = 0
		while num != 0:
			if num % 2 == 0:
				num /= 2
				count += 1
			else:
				num -= 1
				count += 1
		return count
