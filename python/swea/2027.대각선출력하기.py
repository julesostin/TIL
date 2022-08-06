#뭔말인가..싶었는데, #을 0,1,2,3,4칸에 나오게 5줄을 출력해라.라는

for i in range(1,6):
    for j in range(1,6):
        if i == j :
            print("#", end='')
        else:
            print("+", end='')
    print()