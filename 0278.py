# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = 1
        e = n
        while s < e:
            m = (s + e) / 2
            if isBadVersion(m):
                e = m
            else:
                s = m + 1
        return s
