import sys
sys.stdin = open("input2056.txt","r")

T = int(input())

for i in range(1, T+1):
#여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
#테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
    n = input()
    year = n[:4]
    month = n[4:6]
    day = n[6:]
    day_dict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    if(int(month) >13) or (int(month) <= 0):
        print(f'#{i}',-1)
        continue
    else:
        if day_dict[int(month)] < int(day) or int(day) <= 0:
            print(f'#{i}',-1)
            continue
        else:
            print(f'#{i} {year}/{month}/{day}')

#if문에 year이 없는 이유는 년도수는 크게 벗어나는 범위가없고, 달은 12월 날은 31,30,28을 벗어나면 오류이기때문.
#슬라이싱을 이용해 연/월/일을 출력한다.
