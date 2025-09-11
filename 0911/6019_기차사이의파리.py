T = int(input())

# 거,속,시 문제
for tc in range(1, T+1):
    # D는 두 기차 전면부 사이의 거리, A는 기차 A의 속력
    # B는 기차 B의 속력, F는 파리의 속력
    D, A, B, F = map(int, input().split())

    # 두 기차가 충돌하는 데 걸리는 시간
    T = D / (A + B)
    # 파리가 나는 총 거리 = 시간 * 속도
    fly_d = F * T

    print(f"#{tc} {fly_d}")

