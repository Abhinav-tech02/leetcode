class Solution:
    def checkRecord(self, s: str) -> bool:
        absent=0
        late=0
        max_late=0

        for i in s:
            
            if(i=="A"):
                absent+=1
                late=0  
            elif(i=="L"):
                late+=1
                max_late=max(max_late, late)   
            else:
                late=0  

        if(absent<2 and max_late<3):
            return True
        
        return False