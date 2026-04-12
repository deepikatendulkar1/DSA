class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        l,r=m+n-1,n-1
        while r>=0:
            nums1[l]=nums2[r]
            r-=1
            l-=1
        nums1.sort()
        return nums1
        






