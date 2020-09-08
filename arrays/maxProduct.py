def maxProduct(nums):
    result = nums[0]
        temp0 = 1
        temp1 = 1
        first_neg = False
        for num in nums:
            # update first and second product (if need)
            temp0 *= num
            if first_neg:
                temp1 *= num
            # update result
            if first_neg:
                result = max(temp0, temp1, num, result)
            else:
                result = max(temp0, num, result)
            # initilaze next loop
            if not first_neg and num < 0:
                first_neg = True
            if num == 0:
                temp0 = 1
                temp1 = 1
                first_neg = False
    return result   