class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        neg = -1 if x < 0 else 1
        x = abs(x)
        temp = 0
        
        while x != 0:
            rem = x % 10
            
            if temp > (INT_MAX - rem) // 10:
                return 0
                
            temp = (temp * 10) + rem
            x //= 10
            
        return temp * neg