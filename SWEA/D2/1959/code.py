import sys;
sys.stdin = open('input.txt', 'r')

answer = 0
group = []
for tc in range(1, int(input())+1):
    numa, numb = map(int, input().split())
    if numb > numa:
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
    else:
        B = list(map(int, input().split()))
        A = list(map(int, input().split()))
    num = abs(numb - numa)
    C = A[:]
    for i in range(num+1):
        j = num - i
        if j == 0:
            for aa in range(i):
                C.append(0)
        elif i == 0:
            for bb in range(j):
                C.insert(0, 0)
        else:
            for aa in range(i):
                C.append(0)
            for bb in range(j):
                C.insert(0, 0)
        for k in range(len(B)):
            hap = C[k] * B[k]
            answer = hap + answer
        group.append(answer)
        answer = 0
        hap = 0
        C = A[:]
    group.sort()
    print(f'#{tc} {group[-1]}')
    group = []