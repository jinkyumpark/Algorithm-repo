#Defanging an IP Address - from LeetCode 1108

#Runtime: -31.74%, 28ms
#Memory Usage: -73.77%, 14.3MB

class Solution:
    def defangIPaddr(self, address: str)->str:
        defanged = ''
        for i in range(len(address)):
            if address[i] != '.':
                defanged = defanged + (address[i])
            else:
                defanged = defanged +  '[.]'
        return defanged
