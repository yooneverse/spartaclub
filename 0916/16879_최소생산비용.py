import heapq

T = int(input())                         # 테스트 케이스 수

for tc in range(1, T+1):
    N, E = map(int, input().split())     # 마지막 노드 번호, 간선 수
    graph = [[] for _ in range(N+1)]     # 노드 개수만큼 인접 리스트

    for _ in range(E):                   # 간선 입력
        s, e, w = map(int, input().split())
        graph[s].append((e, w))          # 시작 -> (도착, 가중치)

    INF = 1e9
    dist = [INF] * (N+1)                 # 거리 배열
    dist[0] = 0                          # 시작은 0
    pq = [(0, 0)]                        # (거리, 노드)로 큐 시작

    while pq:
        d, now = heapq.heappop(pq)       # 거리, 현재 노드 꺼냄
        if d > dist[now]:                # 이미 더 짧은 거리 있으면 스킵
            continue
        if now == N:                     # 목표 노드 도착했으면 끝
            break
        for nxt, w in graph[now]:        # 연결된 노드 확인
            nd = d + w                   # 현재 거리 + 간선
            if nd < dist[nxt]:           # 더 짧으면 갱신
                dist[nxt] = nd
                heapq.heappush(pq, (nd, nxt))   # 큐에 넣기

    print(f'#{tc} {dist[N]}')            # 0에서 N까지 최단거리
