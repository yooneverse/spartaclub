# 9489. 고대 유적
# 다른 알고리즘을 활용할 수 있다면 적용하여 구해볼까 했으나, 열 탐색-행 탐색 비교 아이디어만 구현해냄. 

T = int(input())                                                  # 테스트 케이스 개수 입력

for tc in range(1, T+1):
    n, m = map(int, input().split())                              # 행 개수 n, 열 개수 m
    matrix = [list(map(int, input().split())) for _ in range(n)]  # n*m 배열 입력

    max_len = 0   # 전체에서 가장 긴 구조물 길이 초기 설정값

    # 열 탐색
    for col in range(m):               # 열 단위 반복
        cnt = 0                        # 연속된 1의 길이
        col_max = 0                    # 현재 열에서 최댓값

        for row in range(n):           # 위에서 아래로 내려가며 탐색
            if matrix[row][col] == 1:  # 1이면 길이 +1
                cnt += 1
                col_max = max(col_max, cnt) # 최대 값 갱신
            else:                      # 0이면 끊기므로 길이 리셋
                cnt = 0

        max_len = max(max_len, col_max)  # 열 최댓값으로 전체 갱신

    # 행 탐색
    for row in range(n):               # 행 단위 반복
        cnt = 0                        # 연속된 1의 길이
        row_max = 0                    # 현재 행에서 최댓값

        for col in range(m):           # 왼쪽에서 오른쪽으로 움직이며 탐색
            if matrix[row][col] == 1:  # 1이면 길이 +1
                cnt += 1
                row_max = max(row_max, cnt) # 최댓값 갱신
            else:                      # 0이면 끊기므로 길이 리셋
                cnt = 0

        max_len = max(max_len, row_max)  # 행 최댓값으로 전체 갱신

    print(f"#{tc} {max_len}")          # 최종 결과 출력




