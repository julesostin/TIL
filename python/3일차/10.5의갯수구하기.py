# 이 통을 순회해라
# 그리고 5를 찾아서 +1을 하고
# 다 돌았으면 멈춰?
# > 주어진 리스트의 요소 중에서 5의 개수를 출력하시오.


numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5] 
list = 0

for rythem in numbers:
    if rythem == int(5):
       list +=1
print(list)
