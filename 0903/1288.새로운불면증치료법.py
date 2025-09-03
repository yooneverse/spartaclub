# 소요시간 42분

# 총 테스트 케이스 수
T = int(input())

# 각 테스트 케이스 처리
for x in range(1, T+1):                  #문제에서 주어진대로 테스트케이스 번호 x로
# 배수 작업을 할 초기 양 번호값 = N
    n = int(input())

# 각 자리수에서 0부터 9까지의 모든 수를 보는 것은 최소 몇 번 양을 센 시점인가??
    nums = [0,1,2,3,4,5,6,7,8,9]

    seen = [0] * 10      # seen에 담고
    cnt = 0              # 다 채워질 때까지 횟수 세기

    i = 0                # xN번에서 x를 나타내는 '인덱스'
    all_seen = 0         # 다 봤을 때의 횟수 저장

    # 여기서 0부터 9 순회에 while이냐 for냐
    # 한 서클씩이니까 while 써보자

    while cnt < 10:               # 10칸 다 세기 전까지
        i += 1                    # 배수로서의 i가 증가
        multi = i * n             # 현재 배수
        all_seen = multi          # 현재 배수를 다 봤을 때, 즉 최대값으로 설정

        s_multi = str(multi)      # 각 숫자를 뽑아내기 위해 문자열로 만들어줌

        for char_digit in s_multi:    # 문자열에서 순회하여 문자 뽑아냄
            digit = int(char_digit)   # 우리가 받을 건 숫자니까 다시 숫자로

            
            if seen[digit] == 0:       # 이 숫자를 처음 보는 것인지 확인
                
                seen[digit] = 1        # 처음 봤으면 봤다고 표시하고
                cnt += 1               # 횟수를 더해준다


                if cnt == 10:  # 모든 값을 다 봤다면
                    break  # 자릿수 순회중단

    print(f'{x} {all_seen}')
