import sys

sys.stdin = open("input1204.txt")

T = int(input())

for t in range(1, T+1):
    tc = int(input())
    score = list(map(int,input().split()))
    # 점수를 인덱스 값으로 하는 리스트를 생성
    score_list = [0] * 101
    # 0이 101개 담겨 있는 score_list를 만든다.

    for i in score:
        score_list[i] += 1
    #받아온 점수 데이터를 순회하면서 해당 점수 인덱스에 +=1 씩 더해주기.

    top_values=max(score)
    result = []

    # 점수의 인원 수를 돌면서 최대값에 해당하면 그 점수(인덱스값)을 top_vcalue에 저장
    for j in range(len(score_list)):
        if max(score_list) == score_list[j]:
            result.append(j)

    print('#{} {}'.format(tc,max(result)))


