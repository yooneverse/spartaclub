T = int(input())

for tc in range(1, T+1):
    n = int(input())

    def count_points(N):
        count = 0
        for x in range(-N, N + 1):
            # x^2 계산
            x_sqrt = x * x
            y = 0
            # y를 0부터 증가시키며 x^2 + y^2 <= N^2 만족하는 최대 y 찾기
            while x_sqrt + y * y <= N * N:
                y += 1
            y -= 1  # 마지막 y는 조건을 넘었기 때문에 원하는 값을 찾기 위해 다시 -1

            count += (2 * y + 1)  # -y ~ +y까지 정수 개수
        return count

    print(f'#{tc} {count_points(n)}')