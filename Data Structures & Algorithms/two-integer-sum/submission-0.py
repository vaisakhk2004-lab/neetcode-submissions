class Solution:
    def twoSum(self,nums,target):
        setup={}
        for i,num in enumerate(nums):
            sec_num=target-num
            if sec_num in setup:
               return [setup[sec_num],i]
            setup[num]=i

     
        

         
        