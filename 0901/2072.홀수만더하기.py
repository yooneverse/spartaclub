# SWEA 2072. 홀수만 더하기
# 문제풀이 시간 20:50 ~ 21:00

T = int(input())            # 테스트 케이스 수

for tc in range(1, T+1):                  # 각 테스트 케이스 별로
    nums = map(int, input().split())    # 첫 줄에 주어지는 10개의 수가 띄어쓰기를 가지므로 split으로 input
    
    odd_sum = 0                # 홀수 합 초기 값을 0으로 시작

    for num in nums:            # 받아온 수 안에서 반복해서 숫자 받아오기
        if num % 2 == 1:        # num이 홀수일 경우
            odd_sum += num      # 홀수 합에 num을 더하기
            
    print(f"#{tc} {odd_sum}")       # 출력 형식대로 테스트 케이스 번호 옆 공백 한 칸 후 결과값
