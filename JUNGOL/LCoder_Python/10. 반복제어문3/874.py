# 반복제어문 3 - 형성평가 6 #874

# 자연수 n을 입력받아 각 문제의 출력예와 같이 출력되는 프로그램을 작성하시오.

ipt = int(input())

if ipt == 1:
    print(1)
else:
    #i 반복문은 줄의 개수를 의미
    for i in range(1, ipt+1):
        #j반복문은 출력되는 빈칸의 수
        for j in range(ipt-i, 0, -1):
            print('  ', end='')
        #k반복문은 출력되는 숫자의 수 (숫자는 순서대로) 
        for k in range(1, i+1):
            print(k, end=' ')
        print()