class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 1
        count = 0
        while 5**x <= n :
            count = count+int(n/5**x)
            x += 1

        return count
