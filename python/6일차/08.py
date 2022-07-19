# 아래 코드는 문자열에서 모음의 개수를 찾는 코드입니다. 
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# output값은 3개가 나와야함.

# word = "HappyHacking"

# count = 0

# for char in word:
#     if char == "a" or "e" or "i" or "o" or "u":
#         count += 1

# print(count)

# 참인 경우 멈추고 올라가서 다시 갯수세고 해야함 / 파이선 튜터 모듈 돌려보니 
# 해피해킹을 차례대로 세고있었음. 그래서 하나하나 if문으로.

word = "HappyHacking"

count = 0

for char in word:
    if (char =='a' or char == 'e' or char == 'i' or char =='o' or char == 'u'):
        count = count+1

print(count)