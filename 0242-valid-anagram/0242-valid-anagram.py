class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False

        counts=defaultdict(int)

        for char_s,char_t in zip(s,t):
            counts[char_s]+=1
            counts[char_t]-=1

        for count in counts.values():
            if count!=0:
                return False
        return True
        
        
            
