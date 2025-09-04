T = int(input())                          # 테스트 케이스 수

for tc in range(1, T + 1):                # 각 테스트 케이스 처리
    n = int(input())                      # 문자열 길이
    s = input()                           # 0과 1로 이루어진 문자열

    now = 0                               # 현재 연속된 1의 길이
    max_cnt = 0                           # 지금까지의 최댓값

    for ch in s:                          # 왼쪽부터 한 글자씩 확인
        if ch == '1':                     # 1이면 연속 유지
            now += 1                      # 현재 연속 길이 1 증가
            if now > max_cnt:             # 최댓값인지 확인
                max_cnt = now             # 최댓값 갱신
        else:                             # 0이면 연속 끊김
            now = 0                       # 현재 연속 길이 초기화

    print(f"#{tc} {max_cnt}")             # 정답 출력
