print("adding from be2 branch")
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]):
        i = 0
        n = len(nums)
        for num in nums:
            if num != 0:
               nums[i] = num
               i += 1
        for x in range(i,n):
            nums[x] = 0
        print(nums)

s = Solution()

s.moveZeroes([1,0,2,0,4,5])
