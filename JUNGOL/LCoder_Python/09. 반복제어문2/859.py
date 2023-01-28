#반복제어문 2 - 형성평가 10 #859

#2부터 9까지의 정수 a와 b를 입력받아 a단부터 b단까지의 구구단을 차례대로 출력하는 프로그램을 작성하시오. 구구단 사이의 공백은 3칸이다.​

a, b = map(int, input().split())

# a와 b의 크기에 따라 interval이 달라지므로 달리 설정
if a > b:
    interval = -1
    b = b - 1
else:
    interval = 1
    b = b + 1

#결과값을 넣을 빈 문자열 선언
string = ''

#구구단은 n*1 부터 n*9까지 있으므로 i를 이에 맞춰 설정
for i in range(1, 10):
    #j는 한줄에서 여러 구구단을 출력할 것이므로 모든 구구단을 +해서 한줄로 출력
    for j in range(a, b, interval):
        #i*j:2는 자릿수를 맞추기 위한 f-string 포맷팅
        print(f'{j} * {i} = {i*j:2}', end = '   ')
    print()
    #str 다시쓰기위해 문자열 초기화
    string = ''

'''
신동민님 풀이방법
a, b = list(map(int, input().split()))

nums = [1,2,3,4,5,6,7,8,9]

if a <= b:
    nums = nums[a-1:b]
else:
    nums = nums[a-1:b-2:-1]

gugu_lst = list(range(1, 10))

for i in gugu_lst:
    for j in nums:
        print(f'{j} * {i} = {j*i:>2}', end = '   ')
    print()
'''