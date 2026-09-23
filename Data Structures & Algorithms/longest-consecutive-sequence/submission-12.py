class Solution:
    def longestConsecutive(self,nums):
        nums=set(nums)
        highest=0
        
        for num in nums:
            if num-1 not in nums:
                  res=0
                  while (num + res) in nums:
                        res+=1
                  highest=max(highest,res)
                  
        return highest
        