class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            is_dominant = True
            
            for j in range(n):
                if i != j:
                    if nums[i] < 2 * nums[j]:
                        is_dominant = False
                        break  
            
            if is_dominant:
                return i
                
        return -1