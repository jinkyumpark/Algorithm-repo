#Unsolved
#Validate IP Address - from Leetcode 468

#return IPv4, IPv6 or neither depending on str format

class Solution:
    def validIPAddress(self, IP: str) -> str:
        if self.isIPv4(IP) == True:
            return 'IPv4'
        elif self.isIPv6(IP) == True:
            return 'IPv6'
        else:
            return 'Neither'

    def isIPv4(self, IPA: str) -> bool:
        IPA += ' '
        count = 0
        count_len = 0
        isIPv4 = True
        while IPA[count] != ' ':
            tmp = ''
            while IPA[count] != '.':
                tmp += IPA[count]
                count += 1
            count_len += 1
            if int(tmp) < 0 or int(tmp) > 0:
                isIPv4 = False
            count += 1
        if count_len is not 4:
            isIPv4 = False
        return isIPv4

    def isIPv6(self, IPA: str) -> bool:
        IPA += ' '
        count = 0
        isIPv6 = True
        valid_haxa_str = ['a', 'b', 'c', 'd', 'e', 'f',
                          'A', 'B', 'C', 'D', 'E', 'F',
                          '1', '2', '3', '4', '5', '6',
                          '7', '8', '9', '0']
        while IPA[count] != ' ':
            tmp = ''
            while IPA[count] != ':':
                tmp += IPA[count]
                count += 1

            #Check the length
            if len(tmp) < 1 or len(tmp) > 4:
                isIPv6 = False
            #Check criteria
            for i in range(len(tmp)):
                if self.findElement(valid_haxa_str, tmp[i]) == False:
                    isIPv6 = False
            count += 1
        return isIPv6

    def findElement(self, in_list: list[str], element: str) -> bool:
        isPresent = False
        for item in in_list:
            if item == element:
                isPresent = True
        return isPresent
