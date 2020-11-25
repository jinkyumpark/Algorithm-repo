#Running Sum of 1d Array - from LeetCode 1480

def runningSum(nums):
    sum_num = 0
    out_nums = []
    for i in range(len(nums)):
        sum_num += nums[i]
        out_nums.append(sum_num)
    return out_nums


def getInput():
    len_num = int(input("Length: "))
    out_num = []
    for i in range(len_num):
        tmp_num = int(input("Element: "))
        out_num.append(tmp_num)
    return out_num


def printArray(in_arr):
    print("[", end="")
    for i in range(len(in_arr)):
        print(in_arr[i], end="")
        if i != len(in_arr) - 1:
            print(end=", ")
    print("]", end="")


in_num = getInput()
out_num = runningSum(in_num)
printArray(out_num)
