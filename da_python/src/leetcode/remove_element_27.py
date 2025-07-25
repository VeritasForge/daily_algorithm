def remove_element(nums: list[int], val: int) -> int:
    cnt = 0
    for _ in range(len(nums)):
        if nums[cnt] == val:
            nums.remove(val)
            nums.append(val)
        else:
            cnt += 1
    return cnt
