def remove_element(nums: list[int], val: int) -> int:
    i = 0
    for j in range(1, len(nums)):
        if nums[i] == val and nums[i] != nums[j]:
            nums[j], nums[i] = nums[i], nums[j]
            i += 1
        elif nums[i] != val:
            i += 1
    return i
