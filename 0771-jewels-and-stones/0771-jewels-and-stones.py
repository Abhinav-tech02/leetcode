class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq={}
        sum=0
        for i in stones:
            if(i not in  freq):
                freq[i]=1
            else:
                freq[i]+=1

        for j in jewels:
            if j in freq:
                sum+=freq[j]

        return sum