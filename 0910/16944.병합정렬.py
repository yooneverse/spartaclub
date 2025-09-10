def merge(left, right):
    global right_first  # 전역 변수로 병합 조건 카운트를 추적
 
    result = [0] * (len(left) + len(right))  # 병합 결과를 저장할 리스트 생성
    l = r = 0                                   # 왼쪽(left), 오른쪽(right) 리스트의 현재 인덱스 초기화
 
    # 병합 조건: 오른쪽 리스트의 마지막 값이 왼쪽보다 작으면 카운트 증가
    if left and right and left[-1] > right[-1]:
        right_first += 1
 
    # 양쪽 리스트 모두에 비교할 값이 남아 있을 때까지 반복
    while l < len(left) and r < len(right):
        if left[l] < right[r]:                  # 왼쪽 값이 더 작으면
            result[l + r] = left[l]            # 왼쪽 값을 병합 결과에 저장
            l += 1                             # 왼쪽 인덱스 증가
        else:                                   # 오른쪽 값이 더 작거나 같으면
            result[l + r] = right[r]          # 오른쪽 값을 병합 결과에 저장
            r += 1                             # 오른쪽 인덱스 증가
 
    # 왼쪽 리스트에 남은 값들을 병합 결과에 복사
    while l < len(left):
        result[l + r] = left[l]
        l += 1
 
    # 오른쪽 리스트에 남은 값들을 병합 결과에 복사
    while r < len(right):
        result[l + r] = right[r]
        r += 1
 
    return result  # 병합이 완료된 정렬 리스트를 반환
 
 
# 병합 정렬 함수
# 리스트를 재귀적으로 분할하고 병합하여 정렬된 리스트를 반환한다
def merge_sort(li):
    if len(li) == 1:  # 리스트 길이가 1이면 정렬 필요 없으므로 그대로 반환
        return li
 
    mid = len(li) // 2  # 리스트를 절반으로 나눌 인덱스 계산
    left = li[:mid]  # 왼쪽 절반 슬라이싱
    right = li[mid:]  # 오른쪽 절반 슬라이싱
 
    left_list = merge_sort(left)  # 왼쪽 리스트에 대해 병합 정렬 호출
    right_list = merge_sort(right)  # 오른쪽 리스트에 대해 병합 정렬 호출
 
    merge_list = merge(left_list, right_list)  # 병합된 정렬 리스트 반환
    return merge_list
 
 
# 테스트 케이스 수 입력
T = int(input())  # 테스트 케이스의 개수를 입력 받음
 
# 각 테스트 케이스에 대해 반복
for tc in range(1, T + 1):
    N = int(input())                       # 배열의 크기 입력
    arr = list(map(int, input().split()))  # 배열 요소 입력
 
    right_first = 0  # 오른쪽이 먼저 복사되는 경우를 세는 변수 초기화
 
    sorted_arr = merge_sort(arr)  # 병합 정렬 수행
 
    # 결과 출력
    print(f'#{tc} {sorted_arr[N // 2]} {right_first}')
