'''
判断一个数是否为质数
'''
def isPrime(num):
    if num == 1:
        return True

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

def hasGroupsSizeX_914( deck):

    """
    :type deck: List[int]
    :rtype: bool
    """
    dic = {}
    for i in deck:
        if i not in dic.keys():
            dic[i] = 1
        else:
            dic[i] += 1
    print(dic)

    minin = min(dic.values())
    if  minin == 1:
        return False

    if isPrime(minin):
        for item in dic.values():
            if item % minin != 0:
                return False
        return True

    min_sqrt = int(minin ** 0.5)
    flag = 0
    for j in range(2, min_sqrt+1):
        for item in dic.values():
            if item % j != 0:
                flag = 0
                break
            else:
                flag = 1
        if flag == 1:
            print(j)
            return True
    return False
