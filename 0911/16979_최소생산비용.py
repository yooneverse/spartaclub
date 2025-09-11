# 현재 공장 번호, 지금까지 누적된 비용을 인수로 하는 함수
def find(curr, cost):
    # 공장 번호를 n까지 가서 전부 처리하면(종료조건)
    if curr == n:
        # 현재비용이랑 비교해서 그 시점의 최소 비용 갱신
        if cost < min_cost[0]:
            min_cost[0] = cost
        return
 
    # 각 제품을 모두 살펴 볼 때
    for i in range(n):
        # 해당 제품이 쓰이지 않았다면
        if not used[i]:
            temp_cost = cost + grid[curr][i]
            # 현재까지의 누적 비용이 최소비용보다 크면 더 안 봐도 됨 (가지치기)
            if temp_cost >= min_cost[0]:
                continue
            # 해당 제품을 채택
            used[i] = True
            # 다음 공장에서 제품 값 알아보기
            find(curr + 1, temp_cost)
            # 선택을 취소해서 원상복구
            used[i] = False
 
# 테스트케이스 수 입력받아옴
T = int(input())
 
# 각 테스트케이스별로 처리
for tc in range(1, T + 1):
    # n : 제품 수
    n = int(input())
    # 제품과 공장번호가 적힌 표
    grid = [list(map(int, input().split())) for _ in range(n)]
    # 채택 여부
    used = [False] * n
    # 누적 값 중 최소 비용 구하기
    min_cost = [10**9]
 
    # 재귀를 통한 탐색
    find(0, 0)
 
    # 결과 출력
    print(f"#{tc} {min_cost[0]}")
