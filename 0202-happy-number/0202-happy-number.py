class Solution:
    def isHappy(self, n: int) -> bool:
        while n != 1 and n != 4:
            n = self.powsum(n)
        return n == 1

    def powsum(self, n: int) -> int:
        total = 0
        while n > 0:            
            rem = n % 10
            total += rem ** 2
            n //= 10            
        return total