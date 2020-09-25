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


'''
Idea: Keep a dictionary with cumulative sums as keys and number of times those sums have appeared as values
Then iterate over array and keep adding value of num. If the current sum - k is already in dictionary we know we have a subarray with sum = k at dict[sum - k]
So if sum - k in dict we can add the total number of times that sum - k has appeared to our count.
Then if the sum is unique we add it to the dict if not we just increment the times we've seen it by 1

If stuck just draw array and write out the cumulative sum. Then you can see all the different times the end - start of a subarray = k

'''