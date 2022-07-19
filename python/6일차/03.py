# # 두 수를 Input으로 받아 합을 구하는 코드이다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# numbers = input().split()
# # print(sum(numbers))

# # TypeError: unsupported operand type(s) for +: 'int' and 'str'

numbers = map(int, input(). split())
print(sum(numbers))

# 숫자 값 이외의 목록이sum()메소드에 직접 제공되서 에러.
# 문자열을 해당하는 숫자로 변환 한 다음 합산해야
# googleing으로 알았는데 왜 map이 들어가야 하는지는 잘 모릅니다.
