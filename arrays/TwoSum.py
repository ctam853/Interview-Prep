 def twoSum(nums: List[int], target: int) -> List[int]:
        map = {}
        for index in range(len(nums)):
            if target - nums[index] not in map:
                map[nums[index]] = index
            else:
                return [index, map[target - nums[index]]]

print(twoSum([2, 7, 3], 9))
