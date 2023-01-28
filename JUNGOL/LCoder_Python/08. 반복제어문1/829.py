# 829 : 반복제어문 1 - 형성평가 3

# 0 부터 100 까지의 점수를 계속 입력 받다가 범위를 벗어나는 수가 입력되면 그 이전까지 입력된 자료의 합계와 평균을 출력하는 프로그램을 작성하시오.

# (평균은 반올림하여 소수 첫째 자리까지 출력한다.)​

#입력받은 수를 저장할 리스트 선언
number_list = list()

#반복문 선언, 입력이 0보다 작거나 100보다 크면 break
while True:
    ipt = int(input())
    if ipt < 0 or ipt > 100:
        break
    #그게 아니라면 리스트에 숫자를 추가
    else:
        number_list.append(ipt)
#문제에서 주어진 대로 출력
print(f'sum : {sum(number_list)}\navg : {round(sum(number_list)/len(number_list), 1)}')