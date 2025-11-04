T = int(input())  # 테스트 케이스 수 입력

# 8방향 델타
d = [(-1, -1), (-1, 0), (-1, 1),
     (0, -1),          (0, 1),
     (1, -1),  (1, 0), (1, 1)]

for tc in range(1, T + 1):
    n, m = map(int, input().split())  # n: 보드 크기, m: 돌 놓는 횟수
    info = [list(map(int, input().split())) for _ in range(m)]  # m번 입력 받기

    # 0=빈칸, 1=흑, 2=백
    board = [[0] * n for _ in range(n)]

    # 중앙 초기 세팅
    mid = n // 2
    board[mid - 1][mid - 1] = 2
    board[mid][mid] = 2
    board[mid - 1][mid] = 1
    board[mid][mid - 1] = 1

    # m번 돌 놓기
    for a, b, color in info:
        r, c = a - 1, b - 1  # 문제 입력: (행, 열, 색)

        board[r][c] = color  # 돌 두기

        # 8방향 검사
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            # 인접칸이 상대 색일 때만 탐색 시작
            if 0 <= nr < n and 0 <= nc < n and board[nr][nc] != 0 and board[nr][nc] != color:
                # 직선으로 계속 진행
                for k in range(2, n):
                    row = r + dr * k
                    col = c + dc * k
                    if not (0 <= row < n and 0 <= col < n):
                        break
                    if board[row][col] == 0:  # 빈칸이면 실패
                        break
                    if board[row][col] == color:  # 같은 색 돌 만나면 뒤집기 실행
                        for f in range(1, k):
                            board[r + dr * f][c + dc * f] = color
                        break

    # 최종 개수 세기
    bl, wh = 0, 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                bl += 1
            elif board[i][j] == 2:
                wh += 1

    print(f"#{tc} {bl} {wh}")
