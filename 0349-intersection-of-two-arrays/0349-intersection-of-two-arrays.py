class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        n1=set(nums1)

        for i in nums2:
            if i in n1  and i not in res:
                res.append(i)
        return res