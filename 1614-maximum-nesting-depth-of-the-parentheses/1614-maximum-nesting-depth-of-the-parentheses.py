class Solution:
    def maxDepth(self, s: str) -> int:
        output,counter=0,0
        for i in s:
            if i=="(":
                counter+=1
                output=max(output,counter)
            elif i==")":
                counter-=1

        return output