# 테스트 케이스 수 입력
T = int(input())

# 병합 정렬 함수
def merge_sort(start, end):
    if start == end - 1:
        return start, end

    mid = (start + end) // 2

    left_s, left_e = merge_sort(start, mid)
    right_s, right_e = merge_sort(mid, end)

    merge(left_s, left_e, right_s, right_e)

    return start, end

# 병합 함수: 두 정렬된 구간을 합쳐줌
def merge(left_s, left_e, right_s, right_e):
    global right_first

    l = left_s
    r = right_s
    n = right_e - left_s
    result = [0] * n
    idx = 0

    first_pick = None  # 이 병합에서 첫 번째 선택된 쪽이 어디였는지 저장

    while l < left_e and r < right_e:
        if arr[l] < arr[r]:
            result[idx] = arr[l]
            if first_pick is None:
                first_pick = 'left'
            l += 1
        else:
            result[idx] = arr[r]
            if first_pick is None:
                first_pick = 'right'
                right_first += 1  # 오른쪽이 첫 선택이면 카운트
            r += 1
        idx += 1

    while r < right_e:
        result[idx] = arr[r]
        r += 1
        idx += 1

    while l < left_e:
        result[idx] = arr[l]
        l += 1
        idx += 1

    for i in range(n):
        arr[left_s + i] = result[i]

# 테스트 케이스 반복
for tc in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    right_first = 0  # 병합에서 오른쪽이 먼저 뽑힌 횟수 초기화
    merge_sort(0, n)

    print(f'#{tc} {arr[n // 2]} {right_first}')