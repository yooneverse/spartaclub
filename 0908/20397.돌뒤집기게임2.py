T = int(input())  # 게임 개수 입력
 
for tc in range(1, T+1):
    n, m = map(int, input().split())          # n: 돌의 수, m: 뒤집기 횟수
    stones = list(map(int, input().split()))  # 돌의 초기 상태 (0: 흰, 1: 검)
 
    for _ in range(m):
        i, j = map(int, input().split())      # i: 중심 위치, j: 확인할 쌍의 개수
        center = i - 1                        # 중심 인덱스 (리스트는 0부터 시작하므로 -1)
 
        # 중심에서부터 좌우로 k칸 떨어진 돌들을 비교 (1칸부터 j칸까지)
        for k in range(1, j+1):
            left_idx = center - k             # 중심에서 왼쪽으로 k칸
            right_idx = center + k            # 중심에서 오른쪽으로 k칸
 
            # 인덱스가 범위를 벗어나면 중지
            if left_idx < 0 or right_idx >= n:
                break
 
            # 마주보는 두 돌의 색이 같으면 둘 다 뒤집기
            #   - 0은 흰색, 1은 검은색이라고 하면
            #   - 1 - x 연산으로 0이면 1이 되고, 1이면 0이 됨
            if stones[left_idx] == stones[right_idx]:
                stones[left_idx] = 1 - stones[left_idx]
                stones[right_idx] = 1 - stones[right_idx]
 
    # 모든 뒤집기 과정을 마친 뒤 최종 상태 출력
    print(f"#{tc}", *stones)
