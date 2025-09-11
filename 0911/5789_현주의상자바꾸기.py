T = int(input())

for tc in range(1, T+1):
    n, q = map(int, input().split())      # n = 상자 개수, q = 쿼리 개수
    arr = [0] * (n+1)                     # 1번부터 n번까지 배열을 준비하되, 여지를 위해 1 추가

    for i in range(1, q+1):               # i = 쿼리 번호
        l, r = map(int, input().split())
        for j in range(l, r+1):           # l ~ r 범위에 i번 값 채우기
            arr[j] = i

    print(f'#{tc}', *arr[1:])             # 1번부터 n번까지 출력
