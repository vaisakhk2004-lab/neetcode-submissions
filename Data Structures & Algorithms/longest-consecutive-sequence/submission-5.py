class Solution:
    def longestConsecutive(self, nums):
        if len(nums) < 2:
            return len(nums)
        nums.sort()
        current_length = 0
        max_length = 0
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:
                current_length += 1
            elif nums[i] == nums[i + 1]:
                pass
            else:
                max_length = max(max_length, current_length + 1)
                current_length = 0
    
        max_length = max(max_length, current_length + 1)
        return max_length
