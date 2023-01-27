import sys;
sys.stdin = open('input.txt', 'r')

N = int(input())
hi = list(map(int, input().split()))
hi.sort()
print(hi[N//2])