def productExceptSelf(nums):
    L, R, output = [0] * len(nums), [0] * len(nums), [0] * len(nums)
    L[0] = 1
    for i in range(1, len(nums)):
        L[i] = L[i - 1] * nums[i - 1]
    R[len(nums) - 1] = 1
    for i in reversed(range(len(nums) - 1)):
        R[i] = R[i + 1] * nums[i + 1]
    for idx in range(len(nums)):
        output[idx] = L[idx] * R[idx]
    return output


print(productExceptSelf([1, 2, 3, 4]))
