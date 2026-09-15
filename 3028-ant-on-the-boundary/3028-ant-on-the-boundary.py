class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        res=0
        curr_pos=0

        for i in nums:
            curr_pos+=i

            if (curr_pos==0):
                res+=1

        return res
        