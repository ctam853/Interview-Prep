# Solution to LC: 560 Subarray Sum Equals K

# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_dict = {0: 1}
        count = 0
        curr_sum = 0
        for num in nums:
            curr_sum += num
            if curr_sum - k in sum_dict:
                count += sum_dict[curr_sum - k]
            if curr_sum in sum_dict:
                sum_dict[curr_sum] += 1
            else:
                sum_dict[curr_sum] = 1
        return count