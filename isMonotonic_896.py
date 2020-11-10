'''
判断数组是否单调

条件；
1、1 <= A.length <= 50000
2、-100000 <= A[i] <= 100000
'''
def isMonotonic_896(A):
    """
    :type A: List[int]
    :rtype: bool
    """

    if len(A) == 1:
        return True
    if A[1] - A[0] > 0:
        for i in range(1, len(A)):
            if A[i] < A[i - 1]:
                return False
    else:
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                return False
    return True



if __name__ == '__main__':
    ret = isMonotonic_896([1, 1,1,1,1,1])
    print(ret)
