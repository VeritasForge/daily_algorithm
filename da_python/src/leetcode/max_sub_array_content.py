# 53. Maximum Subarray (Follow-up)
# 합계가 아닌 '부분 배열 자체'를 반환하는 연습입니다.


def get_max_sub_array_content(nums: list[int]) -> list[int]:
    """
    합이 최대가 되는 연속 부분 배열을 반환합니다.

    작성 가이드:
    1. current_max_sum이 새출발할 때(v 단독 선택), 시작 인덱스를 현재로 옮기세요.
    2. max_sum이 갱신될 때마다, 그때의 시작점과 끝점을 따로 저장해두세요.
    3. 마지막에 저장된 인덱스를 이용해 nums를 슬라이싱(nums[start:end+1])하여 반환합니다.
    """
    if not nums:
        return []

    # TODO: 코드를 완성해 보세요.
    # 인덱스 추적용 변수들
    start = end = c_start = 0

    # 초기값 설정
    m_sum = c_sum = nums[start]
    for i, v in enumerate(nums[1:], start=1):
        if v > c_sum + v:
            c_start = i
            c_sum = v
        else:
            c_sum += v

        if m_sum < c_sum:
            start = c_start
            end = i
            m_sum = c_sum

    return nums[start : end + 1]
