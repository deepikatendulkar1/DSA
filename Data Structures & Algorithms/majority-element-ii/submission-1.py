class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap={}
        for num in nums:
            if num not in hashmap:
                hashmap[num]=1
            else:
                hashmap[num]+=1
        res=[]
        for i in hashmap:
            if hashmap[i]>len(nums)//3:
                res.append(i)
        return res