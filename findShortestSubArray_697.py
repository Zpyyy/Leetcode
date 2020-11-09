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
    m = max(dic.values())
    for key, value in m.items():
        if (value == max(m.values())):
            break
    for index in range(len(nums)):
        if nums[index] == key:
            i = index
            break
    for index in range(len(nums),-1,-1):
        if nums[index] == key:
            j = index
            break
    return j-i
