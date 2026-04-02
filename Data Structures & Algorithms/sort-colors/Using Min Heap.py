class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        heap=[]
        for num in nums:
            heapq.heappush(heap,num)
        for i in range(len(nums)):
            nums[i]=heapq.heappop(heap)
        
