def binary_search(target, sorted_list):
    left = 0                      # 탐색 시작 인덱스
    right = len(sorted_list) - 1  # 탐색 끝 인덱스
    last_direction = 0            # 직전 방향 (0=없음, 1=오른쪽, -1=왼쪽)

    while left <= right:          
        mid = (left + right) // 2  # 중간 인덱스

        # 1) 찾는 값을 발견한 경우
        if sorted_list[mid] == target:
            return True

        # 2) 찾는 값이 mid보다 큰 경우
        #    오른쪽 구간 탐색
        elif sorted_list[mid] < target:
            if last_direction == 1:    # 직전에도 오른쪽이면 실패
                return False
            last_direction = 1
            left = mid + 1             # 탐색 시작 위치를 mid 다음으로 갱신

        # 3) 찾는 값이 mid보다 작은 경우
        #    왼쪽 구간 탐색
        else:
            if last_direction == -1:   # 직전에도 왼쪽이면 실패
                return False
            last_direction = -1
            right = mid - 1            # 탐색 끝 위치를 mid 이전으로 갱신

    return False  # 끝까지 못 찾으면 실패


# 입력
# 테스트 케이스 총 개수
T = int(input())
for tc in range(1, T + 1):                                   # 각 테스트케이스별 처리
    n, m = map(int, input().split())                         # A 크기, B 크기
    sorted_list = sorted(list(map(int, input().split())))   # n개 숫자 받아와서 정렬
    search_list = list(map(int, input().split()))             # m개 숫자 받아오기

    count_valid = 0
    for value in search_list:
        if binary_search(value, sorted_list):  # 조건 충족 검사
            count_valid += 1

    print(f'#{tc} {count_valid}')