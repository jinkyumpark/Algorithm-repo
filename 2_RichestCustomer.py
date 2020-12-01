#Richest Customer Wealth - from Leetcode 1672

#Runtime: +98.2
#Memory Usage: -89.6%

class Solution:
	def maximumWealth(self, accounts:list[list[int]])->int:
		max_wealth = 0
		for i in range(len(accounts)):
			i_wealth = 0
			for j in range(len(accounts[i])):
				i_wealth += accounts[i][j]
			if i_wealth > max_wealth:
				max_wealth = i_wealth
		return max_wealth
