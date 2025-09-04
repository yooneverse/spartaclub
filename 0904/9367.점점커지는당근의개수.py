T = int(input())           # 총 테스트 케이스 수

for tc in range(1, T + 1):
    n = int(input())                    # 당근 수확 수
    c = list(map(int, input().split())) # 당근 크기 값 리스트로

    now = 1  # 연속으로 커지는 길이 세는 변수
    max_cnt = 1  # 최대값 초기 설정

    for i in range(n - 1):
        if c[i] < c[i + 1]:  # 앞 값 < 뒤 값 일 때
            now += 1  # 연속인지 세는 개수에 1 추가
        else:
            now = 1  # 현상유지

        if now > max_cnt:   # 최댓값 갱신
            max_cnt = now

    print(f"#{tc} {max_cnt}")

