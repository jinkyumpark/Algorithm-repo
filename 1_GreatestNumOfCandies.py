#Kids With the Greatest Number of Candies - from LeetCode 1431

#An array is given containing number of candies each kid has
#return bool of whether it is possible to distribute extra candies
#so that each respective kid has the greatest number of candies

#Runtime: -5.55%
#Memory Usage: -83.10%

class Solution():
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        isGreatest: list[bool] = []
        for i in range(len(candies)):
            isGreatest.append(False)

        for i in range(len(candies)):
            candies[i] += extraCandies
            if self.greatestIndex(candies, i) == i:
                isGreatest[i] = True
            candies[i] -= extraCandies
        return isGreatest

#return position of the greatest index
#if there's more than 1 greatest, return provided index given it is one of the greatest
    def greatestIndex(self, in_list: list[int], index: int) -> int:
        greatest = -1
        index_at = -1

        for i in range(len(in_list)):
            if greatest < in_list[i]:
                greatest = in_list[i]
                index_at = i

        if greatest == in_list[index]:
            index_at = index
            
        return index_at
