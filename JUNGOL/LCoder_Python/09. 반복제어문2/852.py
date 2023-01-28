# 반복제어문 2 - 형성평가 3 #852

# 정수를 입력받아서 1부터 입력받은 정수까지의 5의 배수의 합을 구하여 출력하는 프로그램을 작성하시오.​

ipt = int(input())

#누적합을 더할 변수 total을 선언
total = 0

#5로 나누어떨어지면 total에 누적해서 합하기
for i in range(ipt+1):
    if i % 5 == 0:
        total += i

print(total)