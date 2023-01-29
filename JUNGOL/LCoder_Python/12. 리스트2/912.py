# 리스트 2 - 형성평가 3 #912

# 6개의 문자리스트를 ['J', 'U', 'N', 'G', 'O', 'L']이라고 초기화 한 후, 문자 한 개를 입력받아 리스트에서의 위치를 출력하는 프로그램을 작성하시오. 
# 첫 번째 위치는 0번이며 배열에 없는 문자가 입력되면 "none"이라는 메시지를 출력한다.

ipt = input()

chars = ['J', 'U', 'N', 'G', 'O', 'L']

#if - else를 활용해 입력받은 문자가 chars에 없으면 none 출력
if ipt in chars:
    #있으면 for문에서 같으면 해당 인덱스를 출력
    for char in chars:
        if char == ipt:
            print(chars.index(char))
else:
    print('none')