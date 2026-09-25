class Solution:
    def longestConsecutive(self,nums):
        nums=set(nums)
        res=0
        longest=0
        for num in nums:
            if num-1 not in nums:
               res=1
               while num+res in nums:
                    res+=1
            if res>longest:
                longest=res
        return longest
        

        