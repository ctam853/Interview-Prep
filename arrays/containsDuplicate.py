def containsDuplicate(nums : List[int]) -> bool:
    aset = set()
    for num in nums:
        if num in aset:
            return True
        else:
            aset.add(num)
    return False

