class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        s = set()
        try:
            for l in matrix:
                if l[-1] >= target and l[0] <= target:
                    s = set(l)
                    break
            if target in s:
                return True
            return False
        except:
            return False