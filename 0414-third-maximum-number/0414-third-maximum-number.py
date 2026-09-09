class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if(len(nums)<3):
            return max(nums)
        res=list(set(nums))

        res.sort(reverse=True)
        if(len(res)<3):
            return max(res)
        return res[2]