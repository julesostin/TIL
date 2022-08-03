# index
subway = ["이나영" , "윤석빈", "김타키"]

print(subway.index("이나영"))
# 0
# 몇번째 위치인지 알려줌.

print('============================')

# insert
subway.insert(1, "최송희")
print(subway)

# count함수를 사용할때
subway.append("송송")
print(subway)
print(subway.count("김타키"))
