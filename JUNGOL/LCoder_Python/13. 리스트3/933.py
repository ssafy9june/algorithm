# 리스트 3 - 형성평가 5 #933

# 10 미만의 자연수 두 개를 입력받아서 첫 번째 항과 두 번째 항을 입력받은 수로 초기화시킨 후 세 번째 항부터는 전전항과 전항의 합을 구하여 그 합의 1의 자리로 채워서 차례로 10개를 출력하는 프로그램을 작성하시오.

a, b = map(int, input().split())

numbers = list()

for i in range(10):
    if i == 0:
        numbers.append(a)
    elif i == 1:
        numbers.append(b)
    else:
        numbers.append((numbers[i-2]+numbers[i-1])%10)

for i in range(10):
    print(numbers[i], end=' ')