# 반복제어문 3 - 형성평가 2 #870

# 정수 n을 입력 받아, 알파벳 소문자 중 n의 배수 번째 알파벳만 출력하는 프로그램을 작성하시오.​

#정답을 프린트할 빈 문자열 생성
string = ''
#입력받을 숫자를 ipt에 저장
ipt = int(input())
#맨 처음 숫자부터 ipt씩 더해서 해당 숫자의 아스키코드에 맞는 문자열을 저장
for i in range(97+ipt-1, 123, ipt):
    string += chr(i)
#문자열 출력
print(string)