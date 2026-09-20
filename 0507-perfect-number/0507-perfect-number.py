class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
            
        res = 1  
        i = 2
        
        while i * i <= num:
            if num % i == 0:
                res += i
                if i != num // i:
                    res += num // i
            i += 1
                
        return res == num