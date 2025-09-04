T = int(input())

# 단조 증가 수 판별 함수
def is_increasing(num):
    s = str(num)                  # 각 자리 비교 위해 문자열로 변환
    for i in range(len(s) - 1):   # 인접 자리 비교
        if s[i] > s[i + 1]:       # 앞자리 > 뒷자리면 실패
            return False
    return True

for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    max_val = -1   # 단조 증가하는 곱 중 최댓값 저장

    # 모든 쌍 Ai, Aj (i < j)에 대해 확인
    for i in range(n - 1):
        for j in range(i + 1, n):
            product = arr[i] * arr[j]
            if is_increasing(product):   # 곱이 단조 증가 수인지 확인
                if product > max_val:
                    max_val = product

    # 조건 만족하는 값 없으면 -1 그대로 출력
    print(f"#{tc} {max_val}")

