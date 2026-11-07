from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        nums.sort()
        def backtrack(index):
            if index == len(nums):
               result.append(path.copy())
               return 
            path.append(nums[index])
            backtrack(index+1)
            path.pop()
            backtrack(index+1)
        backtrack(0)
        return result
        

    
        