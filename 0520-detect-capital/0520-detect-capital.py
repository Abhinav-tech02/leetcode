class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n=len(word)
        res=0

        for i in word:
            if(i.isupper()):
                res+=1

        return res==n or res==0 or(res==1 and word[0].isupper())

        