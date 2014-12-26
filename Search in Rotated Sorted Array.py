__author__ = 'wangzaicheng'
class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        # write your code here
        if len(A) == 0:
            return -1
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] == target:
                end = mid
            elif A[start] <= A[mid] and A[start] <= target <= A[mid]:
                end = mid
            elif A[start] <= A[mid]:
                start = mid
            elif A[mid] <= A[end] and A[mid] <= target <= A[end]:
                start = mid
            elif A[mid] <= A[end]:
                end = mid

        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1
