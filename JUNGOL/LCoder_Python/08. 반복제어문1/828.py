#828 : 반복제어문 1 - 형성평가 2

#정수를 입력 받다가 0이 입력되면 그 때까지 입력 받은 홀수의 개수와 짝수의 개수를 출력하는 프로그램을 작성하시오.​

#홀수와 짝수를 넣을 리스트를 각각 생성한다
even_number_list = []
odd_number_list = []

#주어진 값이 0이 아니라면 계속 반복한다.
while True:
    ipt = int(input())
    if ipt == 0:
        break
    else:
        #홀수면 홀수 리스트에, 짝수면 짝수 리스트에 저장한다.
        odd_number_list.append(ipt) if ipt % 2 else even_number_list.append(ipt)
print(f'odd : {len(odd_number_list)} \neven : {len(even_number_list)}')