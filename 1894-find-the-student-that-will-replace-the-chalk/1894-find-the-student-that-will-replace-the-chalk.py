class Solution:
    def chalkReplacer(self, chalk: list[int], k: int) -> int:
        # Step 1: Calculate total chalk needed for 1 full round
        total_chalk = sum(chalk)
        
        # Step 2: Skip all complete rounds in O(1) time using modulo
        k %= total_chalk
        
        # Step 3: Find the exact student who runs out of chalk
        for i, count in enumerate(chalk):
            if k < count:
                return i
            k -= count
            
        return -1