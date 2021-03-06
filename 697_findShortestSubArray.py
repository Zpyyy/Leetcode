'''
给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。
你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。

Example 1:
输入: [1, 2, 2, 3, 1]
输出: 2
解释: 
输入数组的度是2，因为元素1和2的出现频数最大，均为2.
连续子数组里面拥有相同度的有如下所示:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组[2, 2]的长度为2，所以返回2.


Example 2:
输入: [1,2,2,3,1,4,2]
输出: 6

'''

def findShortestSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dic = {}
    for i in nums:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1

    print(dic)
    temp = []
    length = []
    for key, value in dic.items():
        if (value == max(dic.values())):
            temp.append(key)
    for temp_key in temp:
        for index in range(len(nums)):
            if nums[index] == temp_key:
                i = index
                break
        for index in range(len(nums)-1,-1,-1):
            if nums[index] == temp_key:
                j = index
                break
        length.append(j-i+1)

    return min(length)


if __name__ == '__main__':
    print(findShortestSubArray( [1, 2, 3, 4, 5]))
