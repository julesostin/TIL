# 아래 코드는 문자열을 입력받아 단어별로 나누는 코드입니다.
# # 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# words = list(map(int, input().split()))
# print(words)
# invalid literal for int() with base
# # input : I'm Tutor 6


words = input().split()
print(words)

# 엥..예제3번이랑 똑같이 써봤더니 얼떨결에 나왔다.....
# 이게머냐...그럼, 한줄로 한번 출력해보자. split빼면 되지뭐.

# words = input()
# print(words)
