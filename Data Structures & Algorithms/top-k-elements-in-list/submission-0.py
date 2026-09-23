class Solution:
    def topKFrequent(self, nums, k):
        from collections import Counter
        length=len(nums) + 1
        count=Counter(nums)
        buckets = []
        for _ in range(length):
            buckets.append([])
        for num in count:
            freq=count[num]
            buckets[freq].append(num)
        top_k=[]
        for i in range(length-1,0,-1):
            for num in buckets[i]:
                top_k.append(num)
                if len(top_k)==k:
                   return top_k
        return top_k
        