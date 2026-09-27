class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        freq={}

        for i in deck:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1

        gcd=0

        for v in freq.values():
            gcd=math.gcd(gcd,v)

        if gcd<2:
            return False
        return True