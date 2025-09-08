# 방법 1. min(N, i-1+j)로 리스트 범위를 넘지 않게 하기 위한 컷라인 설정

T = int(input())         # 게임의 개수

for tc in range(1, T+1):                             # 각 게임별로
    n, m = map(int, input().split())                 # 돌 개수 n, 줄 개수 m
    stones = (list(map(int, input().split())))       # 돌 초기 상태 받기 (0=흰, 1=검 이런 식으로 가정)

    for _ in range(m):
        i, j = map(int, input().split())    # 띄어쓰기 있는 값 입력받기
        color = stones[i-1]                 # 시작 돌 색 (인덱스 주의, 인덱스니까 i번째 구하려면 하나 빼줘야 함)
        
        # i번째 돌부터 j개 돌을 확인하면서 뒤집기
        for k in range(i-1, min(i-1+j, n)):               # i-1은 시작 인덱스, 안전범위 설정하기
            if stones[k] != color:                          # 시작 돌과 색이 다르면 뒤집기
                stones[k] = color                          # 뒤집어서 시작 돌과 같은 색으로 맞춤

    print(f"#{tc}", *stones)  # 결과 출력



# 방법 2. while 문으로 범위 구하기

T = int(input())  # 게임 수

for tc in range(1, T+1):
    n, m = map(int, input().split())        # 돌 개수 n, 줄 개수 m
    stones = list(map(int, input().split()))  # 돌 초기 상태

    for _ in range(m):                                        # m개의 줄로 주어진다고 했으니
        i, j = map(int, input().split())                       #  띄어쓰기 있는 값 입력받기(기준 위치, 뒤집는 개수)
        color = stones[i-1]                                  # 시작 돌의 색

        # while문으로 범위 안전하게 돌리기
        k = i - 1                                          # 시작 인덱스
        while k < i - 1 + j and k < n:              # i-1은 시작 인덱스, j개를 뒤집었을 때의 안전범위 설정하기
            if stones[k] != color:    
                stones[k] = color
                
            k += 1  # 다음 돌로 이동

    print(f"#{tc}", *stones)                            # 뒤집기가 끝난 후의 출력