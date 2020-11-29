#Kids With the Greatest Number of Candies - from LeetCode 1431

#An array is given containing number of candies each kid has
#return bool of whether it is possible to distribute extra candies
#so that each respective kid has the greatest number of candies

def kidsWithCandies(candies, extraCandies):
    isGreatest = []
    for i in range(len(candies)):
        isGreatest.append(False)

    for i in range(len(candies)):
        candies[i] += extraCandies
        indexList = greatestIndex(candies)
        for j in range(len(indexList)):
            if indexList[j] == i:
                isGreatest[i] = True
        candies[i] -= extraCandies
    return isGreatest

def greatestIndex(in_list):
    greatest = -1
    index_at = -1
    index_list = []

    for i in range(len(in_list)):
        if greatest < in_list[i]:
            greatest = in_list[i]
            index_at = i
    index_list.append(index_at)

    for i in range(len(in_list)):
        if in_list[i] == in_list[index_at] and i != index_at:
            index_list.append(in_list[i])
    return index_list

def get_input():
    out_list = []
    num_input = int(input("How many number of input: "))
    for i in range(num_input):
        tmp = int(input("Enter element: "))
        out_list.append(tmp)
    return out_list

def print_list(in_list):
    print("[", end="")
    for i in range(len(in_list)):
        print(in_list[i], end="")
        if i is not len(in_list)-1:
            print(", ", end="")
    print("]", end="")

in_list = get_input()
extra = int(input("Extra Candies: "))
out_list = kidsWithCandies(in_list, extra)
print_list(out_list)
