class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        freq={}

        for i in nums:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        temp,res=0,0
        max_v=0
        for k,v in freq.items():
            temp=max(temp,v)
            if(temp>max_v):
                max_v=temp
                res=k

        return res
