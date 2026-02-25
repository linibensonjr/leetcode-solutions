
from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        verdict = False
        for i in nums:
            if nums.count(i) > 1:
                verdict = True
                break
        return verdict
    
nums = [1, 2, 3, 3]
print(Solution().hasDuplicate(nums))