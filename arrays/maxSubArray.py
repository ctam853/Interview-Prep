def maxSubArray(nums):
    maxSum = nums[0]
    curSum = 0
    for num in nums:
        curSum = max(curSum + num, num)
        maxSum = max(maxSum, curSum)
    return maxSum

    