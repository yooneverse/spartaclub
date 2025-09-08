T = int(input())               # 테스트 케이스 수 입력

for tc in range(1, T+1):
    # 퍼즐이 이미 숫자로 다 채워져 있으니까
    # 빈 리스트에 따로 채우는 방식보다 한 줄씩 읽어서 바로 리스트로 저장
    puzzle = [list(map(int, input().split())) for _ in range(9)]   # 9×9 스도쿠 퍼즐 판

    # 스도쿠가 올바른지 확인하는 세 가지 조건:
    #   1. 각 행(row)에 1~9가 중복 없이 모두 있어야 함
    #   2. 각 열(column)에 1~9가 중복 없이 모두 있어야 함
    #   3. 각 3×3 격자 안에 1~9가 중복 없이 모두 있어야 함

    result = 1       # 기본값은 "성공"으로 놓고, 조건 위반 시 0으로 바꿈

    # 1. 행 검사
    for row in puzzle:                     # 퍼즐의 각 행을 꺼내서
        if len(set(row)) != 9:             # 집합으로 바꿨을 때 원소가 9개가 아니면 (중복 존재)
            result = 0                      # 스도쿠 규칙 위반

    # 2. 열 검사
    for col in zip(*puzzle):               # zip(*puzzle)로 행렬을 전치해서 열을 뽑아옴
        if len(set(col)) != 9:             # 열에서도 중복이 있으면
            result = 0

    # 3. 3×3 격자 검사
    #    시작 좌표 기점으로  9개 격자 돌아가며 순회 ex. (0,0), (0,3), (0,6), (3,0)
    for i in range(0, 9, 3):               # 행 기준 시작점: 0,3,6
        for j in range(0, 9, 3):           # 열 기준 시작점: 0,3,6
            nums = []                      # 현재 3×3 격자의 숫자들을 모을 리스트
            for r in range(i, i+3):        # 격자의 세로 범위
                for c in range(j, j+3):    # 격자의 가로 범위
                    nums.append(puzzle[r][c])
            if len(set(nums)) != 9:        # 모은 숫자를 set으로 바꿔서 9개 아니면 중복 발생
                result = 0

    # 최종 결과 출력, 따로 1일 때 0일 때 안 하고 result로 출력
    print(f"#{tc} {result}")