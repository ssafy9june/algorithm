# 리스트 2 - 형성평가 10 #919

# 5개의 단어를 입력받은 후 문자와 문자열을 한 개씩 입력받아 나중에 입력받은 문자나 문자열이 포함된 단어를 모두 출력하는 프로그램을 작성하시오.

# (입력되는 단어나 문자열의 길이는 100자 이하이고, 찾는 단어가 없으면 "none"이라고 출력한다.)

#주어진 입력 중 위 5개를 단어 리스트로 받아옴
words = [input() for i in range(5)]

#주어진 입력 중 밑 2개를 각각 문자와 문자열로 받아옴
char = input()
chars = input()

#문자한번, 문자열한번 비교하므로 for문을 이용함
for diff in [char, chars]:
    
    #단어 리스트에서 단어 하나를 가지고옴
    for word in words:
        #none 출력을 위한 cnt 변수 선언
        cnt = 0
        
        #char/chars가 word에 있으면 출력
        if diff in word:
            print(word)

        #없으면 cnt를 1씩 더하고 그게 끝까지 가면 none 출력
        else:
            cnt += 1
        if cnt == len(words):
            print('none')