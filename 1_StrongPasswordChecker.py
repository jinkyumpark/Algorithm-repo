#Unsolved
#Strong Password Checker - from LeetCode 420

#it has at least 6 at most 20 character
#it contains at least 1 lower case, 1 upper case, 1 digit
#it doesn't contain 3 repeating character

#return 0 if strong, 0< steps to it takes to make it strong

class Solution():
    def __init__(self):
        self.lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'w', 'x', 'y', 'z']
        self.upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'X', 'Y', 'Z']

    def strongPasswordChecker(self, password:str) -> int:
        count = 0

        while self.containLower(password) is True and self.containUpper(password) is True and self.containNum(password) is True:
            if self.containLower(password) is not True:
                if password < 20:
                    password += 'a'
                    count += 1

            if self.containUpper(password) is not True:
                if password < 20:
                    password += 'A'
                    count += 1

            if self.containNum(password) is not True:
                if password < 20:
                    password += '1'
                    count += 1

        if len(password) < 6+count:
            count += 6 - len(password)

        if len(password) > 20+count:
            count += len(password) - (20+count)

        count += self.repeatingChar(password)

        return count

    def containLower(self, inStr: str) -> bool:
        containLower = False
        for i in range(len(inStr)):
            for j in self.lower:
                if inStr[i] == j:
                    containLower = True
        return containLower

    def containUpper(self, inStr:str) -> bool:
        containUpper = False
        for i in range(len(inStr)):
            for j in self.upper:
                if inStr[i] == j:
                    containUpper = True
        return containUpper

    def containNum(self, inStr: str) -> bool:
        containNum = False
        num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(len(inStr)):
            for n in num:
                if inStr[i] == str(num):
                    containNum = True
        return containNum

    #return repeating instance of str
    def repeatingChar(self, inStr: str) -> int:
        repeat = 0
        count = 0
        while count < len(inStr)-2:
            if inStr[count] == inStr[count+1] and inStr[count] == inStr[count+2]:
                repeat += 1
                count += 2
            count += 1
        return repeat
