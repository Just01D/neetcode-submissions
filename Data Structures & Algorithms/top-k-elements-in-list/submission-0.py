class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for i in nums:
            if i in hashMap:
                hashMap[i] = hashMap[i] + 1
            else:
                hashMap[i] = 1
        
        hashMap = dict(sorted(hashMap.items(), key=lambda x:x[1], reverse = True))
        result = list(hashMap.keys())[:k]
        return result
