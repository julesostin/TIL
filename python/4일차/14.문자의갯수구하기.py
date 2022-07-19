# word에 apple
# word는 i를 순회하다가, i랑 같은값이 있으면 +1
# 그 값을 출력


word = 'apple'
count = 0

for i in word:
    if i == 'a':
        count += 1

print(count)
