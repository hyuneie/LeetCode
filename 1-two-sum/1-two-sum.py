class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         # for i in range(len(nums)):
         #    for j in range(i+1, len(nums)):
         #        if nums[i] + nums[j] == target:
         #            return [i, j]
            
#         pairs = [target - nums for nums in nums]
        
#         for i, pair in enumerate(pairs):
#             if pair in nums and i != nums.index(pair):
#                 return [i, nums.index(pair)]
            
        # HashTable = dict()
        # for i, value in enumerate(nums):
        #     print(i, value)
        #     HashTable[value] = i
        # Pairs = [target - num for num in nums ]
        # for i, Pair in enumerate(Pairs):
        #     if Pair in HashTable and i != HashTable[Pair]:
        #         return [i, HashTable[Pair]]
        # #print(Pairs)
        
        nums_sorted = sorted(nums) #2,7,11,15,3,-6 / 10으로 예시변경
        print(nums_sorted)
        
        i, j = 0, len(nums)-1
        
        while i < j:
            left = nums_sorted[i] 
            right = nums_sorted[j]
            difference = left + right - target
            
            if difference > 0:
                j -= 1
            elif difference < 0:
                i += 1
            else: # difference == 0
                break
                
        if left != right:
            return nums.index(left), nums.index(right)
        else:
            return [i for i, num in enumerate(nums) if num == left]
        
        