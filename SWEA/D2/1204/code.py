import sys;
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
 
    score = [] # 주어진 점수 1000개의 리스트
    score = list(map(int, input().split()))
    freq = [] # 빈도수의 리스트
    num = 1 # 빈도수
 
    score.sort()
 
    for i in range(0, 999):
        if score[i] == score [(i+1)]:
            num = num + 1
        else:
            freq.append(num)
            num = 1
 
    if score[-1] == score[-2]:
        freq.append(1)
 
    freq.sort()
    top = freq[-1] #제일 큰 빈도수의 값
    num = 1
 
    score.sort()
 
    for i in range(0, 999):
 
        if score[i] == score[i+1]:
            num = num + 1
            if num == top:
                answer = score[i-1]
        else:
            num =1
    print(f'#{N} {answer}')
