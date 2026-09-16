from collections import defaultdict
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq=defaultdict(int)

        for num in arr:
            freq[num]+=1

        largest_lucky=-1

        for num,count in freq.items():
            if num==count:
                if num>largest_lucky:
                    largest_lucky=num
        return largest_lucky



        