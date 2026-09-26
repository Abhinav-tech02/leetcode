class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        res=[]
        for i in nums:
            res.append(pow(i,2))

        temp=sorted(res)
        return temp

        