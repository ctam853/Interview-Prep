def threeSum(nums, target):
    nums.sort()
	triplets = []
	for i in range(len(nums) - 2):
		left = i + 1
		right = len(nums) - 1
		while left < right:
			currentSum = nums[i] + nums[left] + nums[right]
			if currentSum == targetSum:
				if [nums[i], nums[left], nums[right]] not in triplets:
					triplets.append([nums[i], nums[left], nums[right]])
				left += 1
				right -= 1
			elif currentSum < targetSum:
				left += 1
			else:
				right -= 1
	return triplets