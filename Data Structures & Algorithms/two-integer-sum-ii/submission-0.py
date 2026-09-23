class Solution:
    def twoSum(self, numbers , target) :
        left = 0
        right = len(numbers)-1
        while left<right:
             required=numbers[left]+numbers[right]
             if required==target:
                 return [left + 1, right + 1]
             elif required<target:
                  left+=1
             else:right-=1

        