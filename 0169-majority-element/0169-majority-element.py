from collections import defaultdict
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count=defaultdict(int)

        for num in nums:
            count[num]+=1
        
        majority=-1
        max_freq=0

        for num,freq in count.items():
            if(freq>max_freq):
                max_freq=freq
                majority=num

        return majority
        