class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        res=0

        for i in range(len(requests)):
            if i==0:
                res+=requests[i]
            else:
                res+=(abs(requests[i]-requests[i-1]))

        return res