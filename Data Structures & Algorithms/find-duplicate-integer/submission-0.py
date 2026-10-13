class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        arr=set()
        for i in range(len(nums)):
            if nums[i] not in arr:
                arr.add(nums[i])
            else:return nums[i]
     


        