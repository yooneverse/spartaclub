T = int(input())                     # 총 테스트 케이스 수 입력

for tc in range(1, T+1):             # 각 테스트 케이스 처리
    pre = list(input())              # 목표 메모리 상태를 문자열로 입력받아 리스트로 저장
    n = len(pre)                     # 메모리 길이를 저장
    
    mem = ["0"] * n                  # 현재 메모리 상태 (초기값은 모두 "0")
    cnt = 0                          # 수정 횟수 초기화

    for i in range(n):               # 왼쪽부터 한 칸씩 확인
        if mem[i] != pre[i]:         # 현재 메모리와 목표 상태가 다르면
            cnt += 1                 # 수정 횟수 더해줌
            for j in range(i, n):    # i번째 이후부터 끝까지 전부 바꿔줌
                mem[j] = pre[i]      # 목표 상태에 맞춰서 덮어쓰기

    print(f"#{tc} {cnt}")            # 출력 형식에 맞게 결과 출력
