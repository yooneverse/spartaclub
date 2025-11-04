# 쉬운 당근 포장

T = int(input())   # 테스트 케이스 수 입력
 
for tc in range(1, T+1):        # 각 테스트 케이스 반복
    N = int(input())            
    carrots = sorted(map(int, input().split()))  # 당근 크기 정렬
 
    ans = 10**8          # 최소 차이값
    possible = False     # 포장 가능한지 여부
 
    # 첫 번째 상자 끝(i), 두 번째 상자 끝(j)
    for i in range(1, N-1):
        # i 경계에서 같은 크기 당근이 걸리면 불가능
        if carrots[i-1] == carrots[i]:
            continue
        for j in range(i+1, N):
            # j 경계에서도 같은 크기 당근이 걸리면 불가능
            if carrots[j-1] == carrots[j]:
                continue
 
            A = i          # 첫 번째 상자 개수
            B = j - i      # 두 번째 상자 개수
            C = N - j      # 세 번째 상자 개수
 
            # 세 상자는 모두 1개 이상이어야 함
            if A == 0 or B == 0 or C == 0:
                continue
 
            # --------- 최대, 최소 직접 비교 ---------
            big = A
            if B > big:
                big = B
            if C > big:
                big = C
 
            small = A
            if B < small:
                small = B
            if C < small:
                small = C
 
            diff = big - small
            # --------------------------------------
 
            if diff < ans:   # 최소 차이 갱신
                ans = diff
            possible = True
 
    if possible:
        print(f"#{tc} {ans}")   # 최소 차이값 출력
    else:
        print(f"#{tc} -1")      # 포장 불가능 시 -1 출력

# 야구선수

T = int(input()) # 테스트 케이스 입력
 
for tc in range(1, T+1):
    N, K = map(int, input().split()) # 띄어쓰기 있는 정수 값
    arr = list(map(int, input().split())) #순회를 위해 리스트로 입력받음
     
    # 최댓값 기준으로만 해서 최댓값이 포함되지 않는 경우를 빠트림
    # 부분집합 개념으로 해서 최댓값이 없어도 구간이 생길 수 있음을 포괄해야 함
     
    arr.sort()  # 정렬 안 하면 구간을 제대로 못 잡음
     
    max_team = 0  # 최대 팀 크기 저장
     
    # i번째 선수를 구간의 최댓값으로 본다
    for i in range(N):
        max_member = arr[i]
        total_member = 0  # 이번 구간에서 몇 명 들어가는지 세는 변수
         
        # i에서부터 왼쪽으로 확인하면서 조건 맞는 선수 세기
        for j in range(i, -1, -1):
            if max_member - arr[j] <= K:  # 차이가 K 이하라면 팀에 넣기
                total_member += 1
            else:
                break  # 정렬돼 있으니까 여기서 끊으면 됨
         
        # 지금까지 나온 팀 크기 중 제일 큰 값으로 갱신
        if total_member > max_team:
            max_team = total_member
     
    # 최종 결과 출력
    print(f"#{tc} {max_team}")
    
# 공굴리기

T = int(input())
 
for test_case in range(1, T+1):
    N = int(input())
    box = [list(map(int, input().split())) for _ in range(N)]
     
    max_roll = 0
     
    dx = [-1,1,0,0]   # 상, 하, 좌, 우
    dy = [0,0,-1,1]
     
    for i in range(N):
        for j in range(N):
            x, y = i, j
            steps = 1   # 출발 칸 포함
 
            while True:
                now_val = box[x][y]
                choose_val = now_val
                next_x, next_y = -1, -1
 
                # 4방향 탐색
                for d in range(4):
                    ni, nj = x + dx[d], y + dy[d]
                    if 0 <= ni < N and 0 <= nj < N:
                        if box[ni][nj] < choose_val:
                            choose_val = box[ni][nj]
                            next_x, next_y = ni, nj
 
                # 이동할 곳 없으면 종료
                if next_x == -1:
                    break
                else:
                    x, y = next_x, next_y
                    steps += 1
 
            # while 끝난 뒤 최대값 갱신
            if steps > max_roll:
                max_roll = steps
             
    # 반드시 test_case 루프 안쪽에서 출력
    print(f"#{test_case} {max_roll}")
    
# 증가하는 사탕 수열

T = int(input())
 
for tc in range(1, T+1):
    A, B, C = map(int, input().split())
    eat = 0
 
    # Step 1: B < C
    if B >= C:
        eat += B - (C - 1)   # 먹은 개수
        B = C - 1            # B를 줄임
    if B < 1:                # 비어버리면 실패
        print(f"#{tc} -1")
        continue
 
    # Step 2: A < B
    if A >= B:
        eat += A - (B - 1)
        A = B - 1
    if A < 1:
        print(f"#{tc} -1")
        continue
 
    print(f"#{tc} {eat}")
    
# 쩜프왕쩰리(백준추가문제)

from collections import deque

N = int(input())                                                 # 게임 구역 가로 세로 길이 N
board = [list(map(int, input().split())) for _ in range(N)]      # 2차원 배열로 board 받아옴

def in_range(r, c):                                              # r과 c를 순회하며 범위를 지키도록 하는 함수
    return 0 <= r < N and 0 <= c < N                             # 범위 출력

visited = [[False] * N for _ in range(N)]                        # 2차원 배열로 확인해야 하기 때문에 모두 False인 배열 만들기

Q = deque()
Q.append((0, 0))
visited[0][0] = True

result = False
while Q:
    r, c = Q.popleft()                                           # 큐에서 현재 위치 꺼내기
    if (r, c) == (N - 1, N - 1):                                 # 오른쪽 아래 끝에 도달하면
        result = True                                            # 도달 가능하다는 표시 남기고
        break                                                    # 반복문 종료

    k = board[r][c]                                              # 현재 칸에 적힌 점프 거리 불러오기
    if k == 0:                                                   # 점프 거리가 0이면 더 이상 이동 불가
        continue                                                 # 다음 루프로 넘어감

    for nr, nc in [(r + k, c), (r, c + k)]:                      # 아래쪽, 오른쪽 방향으로 점프 시도
        if in_range(nr, nc) and not visited[nr][nc]:             # 범위 안이고 방문하지 않았다면
            visited[nr][nc] = True                               # 방문 처리하고
            Q.append((nr, nc))                                   # 큐에 추가

if result:                                                       # 탐색이 끝나고 도착했다면
    print("HaruHaru")                                            # 성공
else:                                                            # 도달하지 못했다면
    print("Hing")                                                # 실패



# 당근 포장 (저번 기출)

# ------------------------------------------------------------
# 문제 요약
# - N개의 당근을 크기순으로 정렬한 뒤, 연속된 3구간(소/중/대)으로 나눈다.
# - 같은 크기의 당근은 같은 상자(같은 구간)에만 있어야 한다.
#   → 경계 인덱스 i, j에서 arr[i-1] == arr[i] 또는 arr[j-1] == arr[j]이면 해당 분할은 불가.
# - 세 상자 모두 비어 있으면 안 된다. (각 구간의 원소 수 ≥ 1)
# - 어떤 상자도 ⌊N/2⌋(정수 나눗셈) 초과한 개수를 담을 수 없다.
# - 위 조건을 만족하는 분할 중에서, 세 상자의 개수 차이(최대-최소)가 최소가 되도록 한다.
# - 가능한 분할이 없으면 -1 출력.
#
# 핵심 아이디어
# - 정렬 후, 두 경계 i, j(첫 경계 i, 두 번째 경계 j)를 완전탐색하여
#   [0..i-1], [i..j-1], [j..N-1] 세 구간의 개수를 A, B, C로 계산한다.
# - 유효성(경계에 같은 값 없음, 각 구간 ≥ 1, 각 구간 ≤ N//2)을 통과하면
#   diff = max(A, B, C) - min(A, B, C) 를 계산해 정답 후보 갱신.
#
# 시간 복잡도: 각 테스트에 대해 O(N^2) (i, j 두 겹 반복)
# N ≤ 1000이라면 파이썬에서도 충분히 동작.
# ------------------------------------------------------------

import sys

input = sys.stdin.readline

T = int(input().strip())  # 총 수확(테스트) 횟수

for tc in range(1, T + 1):
    N = int(input().strip())                 # 당근 개수
    carrots = list(map(int, input().split()))  # 당근 크기 목록
    carrots.sort()                           # 같은 크기가 인접해 있도록 정렬 (경계 판정 및 3구간 분할 용이)

    # 정답(최소 차이) 초기값: 충분히 큰 수로 설정
    INF = 10**9
    ans = INF

    # 유효한 분할을 하나라도 찾았는지 여부
    possible = False

    # 상자 하나가 가질 수 있는 최대 개수(⌊N/2⌋)
    half = N // 2

    # 첫 번째 경계 i: 첫 상자의 끝 인덱스 (구간은 [0..i-1])
    # i는 최소 1이어야 첫 상자가 비지 않으며, 두 경계 j와 마지막 상자를 남겨야 하므로 최대 N-2
    for i in range(1, N - 1):
        # 조건) i 경계에서 같은 크기의 당근이 걸치면 분할 불가
        # ex) ... x | x ...  (왼쪽 끝값과 오른쪽 시작값이 같으면 같은 크기가 둘로 나뉘는 것)
        if carrots[i - 1] == carrots[i]:
            continue

        # 첫 상자 개수(미리 계산)
        A = i
        # 추가 제약) A가 half를 초과하면 해당 i로는 어떤 j를 골라도 불가하므로 바로 continue
        if A > half:
            continue

        # 두 번째 경계 j: 두 번째 상자의 끝 인덱스 (구간은 [i..j-1])
        # j는 최소 i+1이어야 두 번째 상자가 비지 않으며, 마지막 상자도 남겨야 하므로 최대 N-1
        for j in range(i + 1, N):
            # 조건) j 경계에서 같은 크기의 당근이 걸치면 분할 불가
            if carrots[j - 1] == carrots[j]:
                continue

            # 세 구간의 개수 계산
            # [0..i-1] 개수: A = i
            # [i..j-1] 개수: B = j - i
            # [j..N-1] 개수: C = N - j
            B = j - i
            C = N - j

            # 조건) 세 상자 모두 비어 있으면 안 됨 (각 ≥ 1)
            # 범위를 i∈[1..N-2], j∈[i+1..N-1]로 잡았기에 원칙적으로 0이 나올 수 없지만,
            # 안전을 위해 한 번 더 점검.
            if A == 0 or B == 0 or C == 0:
                continue

            # 조건) 어떤 상자도 ⌊N/2⌋ 초과 금지
            if A > half or B > half or C > half:
                continue

            # 여기까지 통과했다면 유효한 분할
            possible = True

            # 세 상자의 개수 차이(불균형도): 최대 개수 - 최소 개수
            # 내장함수 max/min을 쓰면 가독성과 안전성이 높다.
            diff = max(A, B, C) - min(A, B, C)

            # 최소 차이 갱신(최소값 유지 불변식)
            if diff < ans:
                ans = diff

    # 출력 형식에 맞추어 결과 출력
    # 유효한 분할이 없으면 -1
    print(f"#{tc} {ans if possible else -1}")
