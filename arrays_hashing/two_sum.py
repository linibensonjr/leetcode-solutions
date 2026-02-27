
from typing_extensions import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = 0
        verdict = False
        while verdict:
            for i in nums:
                for j in nums:
                    if nums[i] + nums[j+1] == target:
                        verdict = True
                        return [i, j+1]

nums = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(nums, target)) # [0, 1]