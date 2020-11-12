def checkPossibility_665( nums):

    """
    :type nums: List[int]
    :rtype: bool
    """
    de_count = 0
    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] < 0:
            de_count += 1
        if de_count >= 2:
            return False
    return True
