class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        sort = nums1 + nums2
        sort.sort()
        
        half = int(len(sort)/2)
        
        if(len(sort) % 2 != 0):
            return sort[half]
        else:
            return float((sort[half] + sort[half-1])/2)