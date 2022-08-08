class Solution:
    def maxArea(self, height: List[int]) -> int:
         i, j = 0, len(height)-1
         MaxWater = -9999
         while i < j:
             Water = (j-i) * min(height[i], height[j])
             if Water > MaxWater:
                MaxWater = Water
             if height[i] > height[j]:
                j -= 1
             else:
                i += 1
         return MaxWater