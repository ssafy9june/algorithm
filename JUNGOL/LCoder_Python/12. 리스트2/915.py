# 리스트 2 - 형성평가 6 #915

# 100개 이하의 정수를 한 줄로 입력받아 입력 받은 개수를 출력한 후, 입력받은 정수를 차례로 출력하되 그 수가 홀수이면 2배한 값을, 짝수인 경우에는 2로 나눈 몫을 출력하는 프로그램을 작성하시오.

#주어진 숫자들을 리스트로 변환
numbers = list(map(int, input().split()))

#len을 활용해 숫자의 개수 출력
print(len(numbers))

#for문에서 number의 짝수 홀수 여부를 확인해 조건에 맞게 출력
for number in numbers:
    print(number * 2, end=' ') if number % 2 else print(number // 2, end=' ')