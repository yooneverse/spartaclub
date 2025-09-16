T = int(input())                                                  # 테스트 케이스 개수 입력

for tc in range(1, T+1):
    n, m = map(int, input().split())                              # 행 n, 열 m 입력
    matrix = [list(map(int, input().split())) for _ in range(n)]  # n*m 배열 입력

    max_len = 0                                                   # 가장 긴 구조물 길이

    # 열 탐색
    for col in range(m):                  # 열 단위 반복
        cnt = 0                              # 연속된 1의 길이 초기 설정
        for row in range(n):              # 위에서 아래로 탐색
            if matrix[row][col] == 1:     # 1이면 길이 증가
                cnt += 1
            else:                         # 0이면 끊기
                if cnt >= 2:              # 길이가 2 이상일 때만 구조물 인정
                    max_len = max(max_len, cnt)
                cnt = 0
        if cnt >= 2:                      # 마지막까지 이어진 경우 처리
            max_len = max(max_len, cnt)

    # 행 탐색
    for row in range(n):                  # 행 단위 반복
        cnt = 0                              # 연속된 1의 길이 초기 설정
        for col in range(m):              # 왼쪽에서 오른쪽으로 탐색
            if matrix[row][col] == 1:     # 1이면 길이 증가
                cnt += 1
            else:                         # 0이면 끊기
                if cnt >= 2:
                    max_len = max(max_len, cnt)
                cnt = 0
        if cnt >= 2:                      # 마지막까지 이어진 경우 처리
            max_len = max(max_len, cnt)

    print(f"#{tc} {max_len}")             # 결과 출력
