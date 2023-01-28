# 반복제어문 2 - 형성평가 5 #854

# 10개의 정수를 입력받아 입력받은 수들 중 짝수의 개수와 홀수의 개수를 각각 구하여 출력하는 프로그램을 작성하시오.​

#숫자 10개 받기
number_list = list(map(int, input().split()))

#나누어 떨어지면 even리스트를 만들어 len을, 나누어 떨어지지않으면 반대로
print(f'even : {len([number for number in number_list if number % 2 == 0])}')
print(f'odd : {len([number for number in number_list if number % 2 == 1])}')