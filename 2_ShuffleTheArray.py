#Shuffle the Array - from Leetcode 1470

#Shuffle array of the form [x1, x2, ... , xn, y1, y2, ... , yn]
#to [x1, y1, x2, y2, ... , xn, yn]

#Runtime: -94.99%, 52ms
#Memory Usage: -14.58%, 14.5MB

class Solution():
    def shuffle(self, nums:list[int], n: int) -> list[int]:
        out_list: list[int] = []
        for i in range(n):
            out_list.append(nums[i])
            out_list.append(nums[n+i])
        return out_list
