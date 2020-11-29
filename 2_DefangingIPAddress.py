#Defanging an IP Address - from LeetCode 1108

#Faster: -31.74%
#Memory Usage: -73.77%

class Solution:
    def defangIPaddr(self, address: str)->str:
        defanged = ''
        for i in range(len(address)):
            if address[i] != '.':
                defanged = defanged + (address[i])
            else:
                defanged = defanged +  '[.]'
        return defanged
