class Solution:
    def twoSum(self,nums, target):
        numbers={}
        for i,num in enumerate(nums):
            second_number=target-num
            if second_number not in numbers:
               numbers[num]=i
            else:return [numbers[second_number],i]
        