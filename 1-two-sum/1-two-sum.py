class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         # for i in range(len(nums)):
         #    for j in range(i+1, len(nums)):
         #        if nums[i] + nums[j] == target:
         #            return [i, j]
            
        pairs = [target - nums for nums in nums]
        
        for i, pair in enumerate(pairs):
            if pair in nums and i != nums.index(pair):
                return [i, nums.index(pair)]