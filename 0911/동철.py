T = int(input())                          # 테스트케이스 수 입력

for tc in range(1, T+1):                  # 각 테스트케이스 처리
    n, q = map(int, input().split())      # n = 상자 개수, q = 작업 개수
    arr = [0] * (n+1)                     # 1번부터 n번까지 배열 준비 (인덱스 맞추기 위해 n+1)

    for i in range(1, q+1):               # i = 작업 번호 (1번 작업부터 q번 작업까지)
        l, r = map(int, input().split())  # l번 상자부터 r번 상자까지
        for j in range(l, r+1):           # 범위 l ~ r에 대해
            arr[j] = i                    # 해당 상자에 i번 작업 번호 기록

    # 결과 출력 (1번 상자부터 n번 상자까지 출력)
    print(f'#{tc}', *arr[1:])
