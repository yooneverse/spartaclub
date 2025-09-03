T = int(input())    # 총 테스트 케이스 수 입력

for t in range(1, T+1):        # 각 테스트 케이스 반복
    N = int(input())           # 농장의 크기 (NxN)

    farm = [list(map(int, input())) for _ in range(N)]   # N줄에 걸쳐 숫자를 입력받아 2차원 리스트로 저장
    

    total = 0          # 농작물 가치 합을 저장할 변수
    mid = N // 2       # 농장의 정중앙 좌표 (행과 열 모두 mid가 중앙)

    for r in range(N):                  # 전체 행을 순회
        dist = abs(mid - r)             # 중앙 행과의 거리 (위/아래로 얼마나 떨어졌는지)
        start = dist                    # 이 행에서 수확 시작 열 (왼쪽 범위)
        end = N - dist                  # 이 행에서 수확 끝 열 (오른쪽 범위, 슬라이싱처럼 끝은 포함X)

        for c in range(start, end):     # 다이아몬드 범위에 포함되는 열만 순회
            total += farm[r][c]         # 해당 좌표 농작물 가치를 total에 더함

    print(f"#{t} {total}")              # 최종 합 출력