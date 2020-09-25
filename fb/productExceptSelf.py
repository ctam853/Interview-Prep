# Solution to LC: 238 Product of Array Except Self

# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        
        prod = 1
        for i in range(len(nums)):
            output[i] *= prod
            prod *= nums[i]
        
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= prod
            prod *= nums[i]
        
        return output


'''

Idea: Basically multiply all values before during first for loop and multiply all values after during second for loop. 

So multiply nums[0] ... nums[i - 1] going up and multiply nums[len(nums) - 1] ... nums[i + 1] going back.


'''