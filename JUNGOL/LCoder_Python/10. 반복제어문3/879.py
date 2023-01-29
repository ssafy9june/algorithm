# 문자열 1 - 자가진단 6 #879

# 다음과 같이 출력되는 프로그램을 작성하라.

# (각 요소들은 10칸씩 공간을 확보하여 오른쪽으로 정렬하여 출력한다.)​
string_list = ['item', 'count', 'price', 'rate', 
               'pen', '20', '100', '50.5',
               'note', '5', '95', '35.3',
               'eraser', '110', '97', '14.2']

#전체 반복 수를 지정
for i in range(len(string_list)):

    #string list 안에 string들을 리스트로 변환
    string = list(string_list[i])

    #10에서 리스트에 길이를 빼서 남은 수 만큼 공백 입력을 반복
    for j in range(10-len(string)):
        string.insert(0, ' ')

    #리스트를 다시 문자열로 합쳐서 출력, 줄바꾸기 하지않음
    print(''.join(string), end='')

    #네번마다 줄바꾸기를 설정
    if (i+1) % 4 == 0:
        print()