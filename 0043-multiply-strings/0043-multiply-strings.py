class Solution(object):
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        result = [0] * (len(num1) + len(num2))
        
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        for i, d1 in enumerate(num1):
            for j, d2 in enumerate(num2):
                digit_product = (ord(d1) - 48) * (ord(d2) - 48)
                result[i + j] += digit_product
                
        carry = 0
        for i in range(len(result)):
            total = result[i] + carry
            result[i] = total % 10
            carry = total // 10
            
        while len(result) > 1 and result[-1] == 0:
            result.pop()
            
        return "".join(map(str, result[::-1]))