class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        heap=[]
        for num,freq in count.items():
            heapq.heappush(heap,(-freq,num))
        res=[]
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        
