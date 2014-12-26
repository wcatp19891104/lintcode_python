__author__ = 'wangzaicheng'
class Solution:
    """
    @param n: An integers.
    @return: An integer which is the first bad version.
    """

    def findFirstBadVersion(self, n):
        # write your code here
        if n == 0:
            return -1
        start = 1
        end = n
        while start + 1 < end:
            mid = start + (end - start) / 2
            if VersionControl.isBadVersion(mid) is True:
                end = mid
            else:
                start = mid
        if VersionControl.isBadVersion(start) is True:
            return start
        return end
