# 모음열이 주어질때 모음의 갯수 세보기
# 반복문. 문자열 갯수 1씩증가+=1로 써보고
# a,e,i,o,i가 몇개인지.라고 접근
# 

word = input
cnt = 0

for i in word:
    if i == ('a') or ('e') or ('i') or ('o') or ('u'):
        cnt += 1
        print(cnt)

