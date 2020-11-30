#Unsolved
#Verbal Arithmetic Puzzle - from LeetCode 1307

#Each character is decoded as one digit (0-9)
#Every pair of different character they must map to different digits
#Each words[i] and result are decoded as one number without leading zeros
#Sum of numbers on left side will eqaul to the number on right side

class Solution:
	def __init__():
		self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
		'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

	def isSolvable(self, words, result):


	def isMoreThan(word, result):
		appeared = []
		criteria = True
		combined = ''
		#Combine word, result in one string

		#Check whether 
		for i in range(len(word)):
			tmp = -1
			for al in alphabet:
				if al == word[i]:
					tmp = i
			 for index in appeared:
			 	if tmp == index:
			 		criteria = False
			 appeared.append(tmp)
