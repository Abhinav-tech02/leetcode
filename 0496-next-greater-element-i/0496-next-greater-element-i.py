class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res=[]

        for i in nums1:
            idx=nums2.index(i)
            found=False
            for j in range(idx+1,len(nums2)):
                if nums2[j]>nums2[idx]:
                    found=True
                    res.append(nums2[j])
                    break

            if not found:
                res.append(-1)

        return res
                
        