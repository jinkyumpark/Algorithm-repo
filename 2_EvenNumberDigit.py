#Unsolved
#Find Numbers with Even Number of Digits - from Leetcode 1295

#Return number of even number of digit in an array

class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0
        for item in nums:
            if self.isDigitEven(item) is True:
                count += 1
        return count

    def isDigitEven(self, num: int) -> bool:
        count = 0
        divisor = 10
        remainder = -1
        while remainder is not num:
            remainder = num % divisor
            divisor *= 10
            count += 1
        if count % 2 is 0:
            return True
        else:
            return False
