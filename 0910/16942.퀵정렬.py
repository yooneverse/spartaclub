# 퀵 정렬 함수
def quicksort(A, l, r):
    if l < r:
        p = partition(A, l, r)  # 기준 원소 위치를 찾고
        quicksort(A, l, p - 1)  # 기준보다 왼쪽 정렬
        quicksort(A, p + 1, r)  # 기준보다 오른쪽 정렬

# 파티션 함수 (Hoare 방식 수정)
def partition(A, l, r):
    p = A[l]  # 첫 번째 원소를 기준으로 사용
    i = l + 1
    j = r

    while True:
        # 왼쪽부터 기준보다 큰 값 찾기
        while i <= r and A[i] <= p:
            i += 1
        # 오른쪽부터 기준보다 작은 값 찾기
        while j >= l and A[j] > p:
            j -= 1
        # 인덱스 교차 시 반복 종료
        if i > j:
            break
        # 잘못된 위치에 있는 값들 교환
        A[i], A[j] = A[j], A[i]

    # 기준 원소와 j 위치의 값 교환
    A[l], A[j] = A[j], A[l]
    return j  # 기준 원소 위치 반환

# 테스트 케이스 처리
T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 정수 개수
    A = list(map(int, input().split()))  # 정수 리스트 입력

    quicksort(A, 0, N - 1)  # 퀵 정렬 수행

    print(f'#{tc} {A[N // 2]}')  # 정렬 후 중간값 출력
