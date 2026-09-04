class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res=[]
        res1=[]

        for i in range(rowIndex+1):
            temp=[1]*(i+1)

            for j in range(1,i):
                temp[j]=res[i-1][j-1]+res[i-1][j]
            res.append(temp)

            if(i==rowIndex):
                res1=res[i]

        return res1