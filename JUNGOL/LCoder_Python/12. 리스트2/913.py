# 리스트 2 - 형성평가 4 #913

# 공백으로 구분하여 입력된 세자리 이하의 정수를 리스트로 받아서 입력된 최대값과 최소값을 출력하는 프로그램을 작성하시오.

#주어진 숫자들을 리스트로 받음
numbers = list(map(int, input().split()))

for i in range(len(numbers)):
    #min과 max에 첫번째값을 넣고 그 이후로 값들과 비교해서 min max 구하기
    if i == 0:
        max = numbers[i]
        min = numbers[i]
    else:
        if numbers[i] > max:
            max = numbers[i]
        if numbers[i] < min:
            min = numbers[i]
print(f'max : {max}\nmin : {min}')