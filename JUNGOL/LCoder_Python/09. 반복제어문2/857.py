#반복제어문 2 - 형성평가 8 #857

#행과 열의 수를 입력받아 다음과 같이 출력하는 프로그램을 작성하시오

#두개의 숫자를 받아서 변수에 저장한다
#sero -> 줄이 몇번 반복되는지
#garo -> 줄안에서 몇번 반복이 일어나는지
sero, garo = map(int, input().split())

for i in range(1, sero+1):
    for j in range(1, garo+1):
        #garo가 1이면 첫번째의 반복이므로 string을 시작한다
        if j == 1:
            string = str(i*1)
        #garo가 1이 아니면 이미 string이 있으므로 뒤에 +로 덧붙힌다
        else:
            string += ' ' + str(i*j)
    print(list)