class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        target_asci=ord(target)
        ascii_codes = [ord(char) for char in letters]
        min_asc=float('inf')
        res_chr=""
        for i in ascii_codes:
            
            temp=i-target_asci
            if temp > 0 and temp < min_asc:
                min_asc = temp
                res_char = chr(i)
        
        return res_char if min_asc != float('inf') else letters[0]