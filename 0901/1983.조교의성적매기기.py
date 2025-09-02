# SWEA_1983. 조교의 성적 매기기
# 풀이 시간: 22:10 ~ 22:40

T = int(input())                              # 테스트 케이스 총 개수 먼저 입력받음

grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']     # 학점 리스트 만들어둠

for tc in range(1, T + 1):                    # 테스트 케이스 하나씩 처리 시작
    N, K = map(int, input().split())          # 학생 수랑 K번 학생 번호 입력

    totals = []                               # 학생들 점수 합 저장할 리스트
    for i in range(1, N + 1):                 # 학생 수만큼 반복 돌리기
        m, f, a = map(int, input().split())   # 중간, 기말, 과제 점수 입력받음
        totals.append(35*m + 45*f + 20*a)     # 가중치 곱해서 총점 계산해서 리스트에 넣기

    k_total = totals[K-1]                     # K번 학생 점수 가져오기
                                              # 0번부터 번호 매겼는데 학생 번호는 1번부터라 -1 해줌

    higher = 0                                # K번보다 점수 높은 학생 수 세는 변수
    for t in totals:                          # 전체 학생 점수 돌면서 확인
        if t > k_total:                       # 만약 점수가 K보다 크면
            higher += 1                       # 높은 학생 수 +1

    rank = higher                             # 순위는 높은 애들 수로 결정됨
    bucket = N // 10                          # 한 학점당 들어가는 학생 수
    grade = grades[rank // bucket]            # 순위 나눈 값으로 학점 뽑아오기

    print(f"#{tc} {grade}")                   # 결과 출력

'''
(미성)
rank = higher로 순위를 잡고 grade = grades[rank // bucket]에서 학점을 뽑는데, 이때 // bucket을 하는 이유는 무엇인가요?
만약 학생 수가 20명이고 학점은 10등급이라면, 왜 순위를 그냥 나누는 게 아니라 bucket으로 나눠서 인덱스로 사용해야 할까요? 

(지윤)
higher로 높은 점수가 1등부터 되도록 내림차순으로 정렬한 점수를 기준으로bucket을 등급당 학생 수로 정해서 rank // bucket으로 묶어줬어요. 
그렇게 해야 순위가 등급 구간별로 나눠져서 grades 배열 인덱스에 대응될 수 있더라구요. 핵심은 '구간' 나눠서 대응시키기인 거 같습니다.
'''