#Find Numbers with Even Number of Digits - from Leetcode 1295

#Return number of even number of digit in an array

#Runtime: +13.77%
#Memory Usage: -39.78%

#Lesson learnt: 'is' is not equal to ==

class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0
        for item in nums:
            if self.isDigitEven(item) == True:
                count += 1
        return count

    def isDigitEven(self, num: int) -> bool:
        count = 0
        divisor = 10
        remainder = -1
        while remainder != num:
            remainder = num % divisor
            divisor *= 10
            count += 1
        if count % 2 == 0:
            return True
        else:
            return False
