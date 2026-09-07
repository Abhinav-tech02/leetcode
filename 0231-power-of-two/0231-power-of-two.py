class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
            
        for i in range(n):
            temp = pow(2, i)
            
            if temp == n:
                return True
            
            if temp > n:
                return False
                
        return False