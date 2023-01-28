#반복제어문 2 - 형성평가 6 #855

#두 개의 정수를 입력받아 작은 수부터 큰 수까지 3의 배수이거나 5의 배수인 수들의 합과 평균을 출력하는 프로그램을 작성하시오. (평균은 반올림하여 소수 첫째자리까지 출력한다.)​

#두개의 숫자를 받아서 각각의 변수에 넣는다
number_small, number_large = map(int, input().split())

#두개의 숫자중 작은것과 큰것을 판단한다
if number_large < number_small:
    number_small, number_large = number_large, number_small

#합과 평균을 구할 조건에 맞는 숫자 리스트를 만든다
number_list = list()

#조건에 맞으면 리스트에 추가한다
for i in range(number_small, number_large+1):
    if i % 3 == 0 or i % 5 == 0:
        number_list.append(i)

#문제에서 주어진대로 프린트한다
print(f'sum : {sum(number_list)}')
print(f'avg : {round(sum(number_list) / len(number_list), 1)}')