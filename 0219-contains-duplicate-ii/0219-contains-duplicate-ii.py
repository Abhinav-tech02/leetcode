class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Think of this as a memory of where we saw each number: {number: index}
        seen = {}
        
        for i in range(len(nums)):
            current_number = nums[i]
            
            if current_number in seen and abs(i - seen[current_number]) <= k:
                return True
                
            seen[current_number] = i
            
        return False