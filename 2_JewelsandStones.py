#Jewels and Stones - from Leetcode 771

#Runime: +51.72%
#Memory Usage: -38.34%

class Solution:
	def numJewelsInStones(self, J: str, S: str)->int:
		count = 0
		for s in range(len(S)):
			for j in range(len(J)):
				if S[s] == J[j]:
					count += 1
		return count
