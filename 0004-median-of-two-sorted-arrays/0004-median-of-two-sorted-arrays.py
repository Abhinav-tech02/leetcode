class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1.sort()
        nums2.sort()

        res = []
        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1

        while i < len(nums1):
            res.append(nums1[i])
            i += 1

        while j < len(nums2):
            res.append(nums2[j])
            j += 1

        n = len(res)

        if n % 2 != 0:
            return float(res[n // 2])
        else:
            return (res[n // 2] + res[(n // 2) - 1]) / 2.0