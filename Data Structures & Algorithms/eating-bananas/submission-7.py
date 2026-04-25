class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        res=r
        while l<=r:
            k=(l+r)//2
            totalhours=0
            for num in piles:
                totalhours+=math.ceil(num/k)
            if totalhours<=h:
                res=k
                r=k-1
            else:
                l=k+1
        return res
