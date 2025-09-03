T = int(input())          # 총 테스트 케이스 수

for tc in range(1, T+1):   # 각 테스트 케이스 처리
    n = int(input())       # 숫자 입력인데 띄어쓰기 없는 하나의 수니까 int를 input만
    prime = [2,3,5,7,11]   # 밑의 모음
    times = [0] * 5        # 숫자 다섯개에 대한 a,b,c,d,e 값을 배열로 만들 토대


    for i in range(5):                # prime이 5개이기 때문에, 5의 범위 내에서 순회
        while n % prime[i] == 0:      # prime 숫자로 나누어서 구한 값이 0이 될 때까지
                times[i] += 1             # 각 i마다 1씩 증가하도록 하면서 배열 각 칸에 숫자를 더해줌
                n = n // prime[i]         # n은 각 i가 나눈 몫으로서 갱신을 진행함


    print(f"#{tc}", *times)

    

