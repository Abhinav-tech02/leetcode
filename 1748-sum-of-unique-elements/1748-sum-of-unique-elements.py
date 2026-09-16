from collections import defaultdict
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count=defaultdict(int)
        sum=0

        for num in nums:
            count[num]+=1

        for n,freq in count.items():
            if(freq>=2):
                continue
            sum+=n
        return sum
        