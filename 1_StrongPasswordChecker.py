#Password is strong iff
#it has at least 6 at most 20 character
#it contains at least 1 lower case, 1 upper case, 1 digit
#it doesn't contain 3 repeating character

#return 0 if strong, 1-5 how many steps to take to make it strong
def strongPasswordChecker(password):
    count = 0
    if len(password) < 6 or len(password) > 20:
        count += 1
    if containLower(password) == False:
        count += 1
    if containUpper(password) == False:
        count += 1
    if containNum(password) == True:
        count += 1
    if repeatingChar(password) == True:
        count += 1
    return count

def containLower(inStr):
    containLower = False
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
             'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'w', 'x', 'y', 'z']
    for i in range(len(inStr)):
        for j in lower:
            if inStr[i] == j:
                containLower = True
    return containLower

def containUpper(inStr):
    containUpper = False
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
             'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'X', 'Y', 'Z']
    for i in range(len(inStr)):
        for j in upper:
            if inStr[i] == j:
                containUpper = True
    return containUpper

def containNum(inStr):
    containNum = False
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(len(inStr)):
        for n in num:
            if inStr[i] == str(num):
                containNum = True
    return containNum

def repeatingChar(inStr):
    repeat = False
    for i in range(len(inStr)-3):
        if inStr[i] == inStr[i+1] and inStr[i] == inStr[i+2] and inStr.index[i+1] == inStr.index[i+2]:
            repeat = True
    return repeat

password = input("Password: ")
print(strongPasswordChecker(password))
