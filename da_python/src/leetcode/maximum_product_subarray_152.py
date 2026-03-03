# https://leetcode.com/problems/maximum-product-subarray/
# 152. Maximum Product Subarray
# Medium


def max_product(nums: list[int]) -> int:
    """
    배열 nums에서 곱이 최대가 되는 연속 부분 배열의 곱을 반환합니다.

    학습 포인트:
    1. 카데인 알고리즘의 '선택' 논리를 곱셈에 적용해보세요.
    2. 음수와 음수가 곱해지면 양수가 된다는 점을 고려하여 최솟값(min)도 함께 추적해야 합니다.
    3. 0을 만났을 때 어떤 처리가 필요한지 고민해보세요.
    """
    if not nums:
        return 0

    # 초기값 설정
    res = max_cur = min_cur = nums[0]

    for i in range(1, len(nums)):
        v = nums[i]

        # TODO: 여기에 로직을 완성해보세요.
        # 힌트: v가 음수일 때 max_cur와 min_cur가 뒤바뀔 수 있습니다.
        # temp_max = max(v, v * max_cur, v * min_cur)
        # ...

        # res = max(res, max_cur)

    return res
