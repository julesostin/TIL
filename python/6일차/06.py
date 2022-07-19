# 아래 코드는 1부터 N까지의 숫자에 2를 곱해서 변수에 저장하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# output [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# tuple은 list와 거의 같지만, 데이터를 변경할 수 없다는 차이가 있습니다.
# 따라서 appen() 등 값을 변경하는 메소드는 사용할 수 없고 조회를 하는
# count(). index() 메소드만 사용할 수 있습니다. 

# number의 type 은 int
#() 소괄호로 이루어진 튜플은 값 수정이나 삭제,추가를 할 수 없으니
# append로 값을 추가하려면 대괄호로 리스트를 만들기**

N = 10
answer = []
for number in range(N + 1):
    answer.append(number * 2)

print(answer)