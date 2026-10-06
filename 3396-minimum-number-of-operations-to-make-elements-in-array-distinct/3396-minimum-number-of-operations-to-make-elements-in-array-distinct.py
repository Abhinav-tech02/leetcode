class Solution(object):
    def minimumOperations(self, nums):
        
        if len(nums) == len(set(nums)) :
            return 0 
        if len(nums) < 4 :
            return 1 
        res = 0 
        size = len(nums) // 3 
        for i in range(size) :
            res += 1 
            for j in range(3) :
                nums.pop(0)
            if len(nums) == len(set(nums)) :
                return res
        return res + 1 