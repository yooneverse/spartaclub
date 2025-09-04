T = int(input()) # 총 테스트 케이스 수


def bus_move(k, n, stop):
    last = 0  # 마지막 충전 위치
    bus = k  # 현재 버스가 갈 수 있는 최대 위치
    cnt = 0  # 충전 횟수

    while bus < n:  # 아직 도착지점(n)에 도착하지 못했다면
        # 뒤로 가면서 충전소 찾기
        while bus > last and stop[bus] == 0:  # 현재 위치에 충전소가 없으면 한 칸씩 뒤로 이동
            bus -= 1

        # 만약 충전소가 아예 없어서 last까지 되돌아왔다면
        if bus == last:  # 이전 충전 위치와 같아졌다는 건 충전 불가라는 의미
            return 0

        # 충전 성공
        last = bus  # 현재 위치를 마지막 충전 위치로 갱신
        cnt += 1  # 충전 횟수 +1
        bus += k  # 충전했으니 다시 k만큼 전진

    return cnt  # 도착지에 도달했을 때 총 충전 횟수 반환


for tc in range(1, T + 1):
    k, n, m = map(int, input().split())
    charge_list = list(map(int, input().split()))  # 충전기가 있는 정류장 리스트

    stop = [0] * (n + 1)  # 정류장 리스트 만들기

    for i in charge_list:  # 충전기가 있는 정류장이라면
        stop[i] = 1  # 1로 표시해줌

    ans = bus_move(k, n, stop)
    print(f"#{tc} {ans}")

