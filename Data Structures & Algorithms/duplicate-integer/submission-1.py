class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers={}
        for num in nums:
            if  num not in numbers:
                numbers[num]=1
            elif num in numbers:
                 return True
        return False