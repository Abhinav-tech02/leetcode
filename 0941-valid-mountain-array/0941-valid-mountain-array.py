class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        n=len(arr)

        if n<3:
            return False

        left,right=0,n-1

        while left+1<n and arr[left]<arr[left+1]:
            left+=1

        while right>=0 and arr[right]<arr[right-1]:
            right-=1
        
        return 0<left==right <n-1
