class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}
        res = []
        
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        top_k = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:k]

        for item in top_k:
            res.append(item[0]) 
        
        return res
