from typing import List
class Solution:
    def __init__(self):
        self.index0 = 0
        self.result = []
        
    def twoSum(self, nums: List[int], target: int):
        if len(nums) > 0:
            initial = nums[0]
            for (index, value) in list(enumerate(nums))[1:]:
                if((value + initial) == target):
                    self.result.extend([self.index0,self.index0+index])
                    return self.result
        else:
            return None
        
        self.index0 += 1
        return self.twoSum(nums[1:],target)