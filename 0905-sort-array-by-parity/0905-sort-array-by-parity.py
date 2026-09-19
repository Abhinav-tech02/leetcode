class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        res1=[]
        res2=[]

        for i in range(len(nums)):
            if(nums[i]%2==0):
                res1.append(nums[i])
            else:
                res2.append(nums[i])

        temp=res1+res2

        return temp
        