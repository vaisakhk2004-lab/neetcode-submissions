class Solution:
    def hasDuplicate(self, nums):
        superb = []                   
        for number in nums:
            if number in superb:      
               return True
            superb.append(number)      
        return False

            
        