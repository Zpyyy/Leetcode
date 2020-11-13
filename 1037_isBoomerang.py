
'''
判断三点是否在一条直线上，只需判断人一两点间斜率是否相等
注意没有斜率的情况
'''


def isBoomerang_1037(points):

    """
    :type points: List[List[int]]
    :rtype: bool
    """
    dy1 = points[0][1] - points[1][1]
    dx1 = points[0][0] - points[1][0]

    dy2 = points[0][1] - points[2][1]
    dx2 = points[0][0] - points[2][0]

    if dx1 and dx2 != 0:
        if dy1/dx1 == dy2/dx2:
            return False
        else:
            return True

    elif dx1 == dx2:
            return False
    else:
            return True


if __name__ == '__main__':
    ret = isBoomerang_1037([[1,1],[2,2],[3,3]])
    print(ret)
