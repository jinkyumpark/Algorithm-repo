#unsolved

#Check if two string arrays are equivalent - from Leetcode 1662

class Solution:
	def arrayStringsAreEqual(self, word1:list[str], word2:list[str])->bool:
		isEqual = True
		word1_parse = self.parseString(word1)
		word2_parse = self.parseString(word2)

		word1_parse.sort()
		word2_parse.sort()

		for i1 in word1_parse:
			for i2 in word2_parse:
				if i1 != i2:
					isEqual = False

		return isEqual


	def parseString(self, in_list:list[str])->list[str]:
		out_list = []
		for word in in_list:
			for i in range(len(word)):
				out_list.append(word[i])
		return out_list
