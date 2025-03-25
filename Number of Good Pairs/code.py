class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        hash={}
        res=0

        for i in nums:
            if i not in hash:
                hash[i]=0
            else:
                hash[i]+=1
                res+=hash[i]
       
               
        return res
