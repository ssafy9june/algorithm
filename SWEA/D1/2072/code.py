import sys;
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    numbers = list(map(int, input().split()))
    addup = []
    for i in range(0, 10):
        if numbers[i]%2 != 0:
            addup.append(numbers[i])
    print(f'#{test_case} {sum(addup)}')