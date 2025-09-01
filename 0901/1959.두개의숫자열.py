# SWEA_1959. 두 개의 숫자열
# 풀이 시간: 23:20 ~ 23:40


T = int(input())                              # 테스트 케이스 총 개수 먼저 입력받음

for tc in range(1, T + 1):                    # 테스트 케이스 하나씩 처리 시작
    n, m = map(int, input().split())          # 두 수 n, m 입력받기
    Aj = list(map(int, input().split()))      # n개의 정수 입력받아 리스트 Aj에 저장
    Bj = list(map(int, input().split()))      # m개의 정수 입력받아 리스트 Bj에 저장


    if n > m:                                 # n이 m보다 크다고 가정
        n, m = m, n                           # n이 항상 더 짧게 만들기 위해서는 바뀌어야 함
        Aj, Bj = Bj, Aj                       # 리스트도 같이 바꿔줘야 함

    max_sum = 0                               # 최댓값 저장 변수
    for i in range(m - n + 1):                # 짧은 리스트가 움직일 수 있는 범위
        curr = 0                              # 현재 위치에서의 합
        for j in range(n):                    # 짧은 리스트 길이만큼 곱셈
            curr += Aj[j] * Bj[i + j]         # 마주보고 있는 같은 위치 값끼리 곱해서 더함
        if curr > max_sum:                    # 최댓값 갱신 조건
            max_sum = curr                    # 최댓값 갱신

    
    print(f"#{tc} {max_sum}")                 # 최댓값을 구해서 결과 출력
