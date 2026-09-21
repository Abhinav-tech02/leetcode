class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        total_product = 1
        zero_count = nums.count(0)
        
        if zero_count > 1:
            return [0] * len(nums)
            
        for num in nums:
            if num != 0:
                total_product *= num
                
        answer = []
        for num in nums:
            if zero_count == 1:
                if num == 0:
                    answer.append(total_product)
                else:
                    answer.append(0)
            else:
                answer.append(total_product // num)
                
        return answer