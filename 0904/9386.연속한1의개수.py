T = int(input())           # 총 테스트 케이스 수

for tc in range(1, T + 1):
    n = int(input())                    # 수열의 길이
    c = list(map(int, input().split())) # 배열 리스트로 받아옴

    now = 1  # 연속으로 커지는 길이 세는 변수
    max_cnt = 1  # 최대값 초기 설정

    for i in range(n - 1):