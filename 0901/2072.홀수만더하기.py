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


'''
(미성) 
nums = map(int, input().split())에서 map 객체를 그대로 사용했는데, 이걸 리스트로 변환하지 않아도 되는 이유는 무엇인가요? 
(지윤) 
map(int, input().split())은 반복 가능한 값을 주기 때문에 별도로 리스트에 담지 않아도 for num in nums:에서 바로 쓸 수 있습니다.
이 문제처럼 한 번만 쓰이는 경우에는 굳이 list()로 바꿀 필요가 없다고 생각해서 그렇게 했습니다! 인덱스로 접근하는 문제면 미성님처럼 하면 좋을 거 같아요.
'''