class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        curr_result = 0
        result = 0
        
        for num in nums:
            
            if num:
                curr_result += 1
            else:
                result = max(result, curr_result)
                curr_result = 0
        
        return max(result, curr_result)