A = int(input())
numbers = list(map(int, input().split()))
dp = {}
prev = {}
answer = 0
for i in range(len(numbers)):
    number = numbers[i]
    dp[i] = 0
    prev[i] = -1
    for j in dp:
        if number > numbers[j] and dp[j] > dp[i]:
            dp[i] = dp[j]
            prev[i] = j
    dp[i] += 1
    if dp[i] > dp[answer]:
        answer = i
answer_list = []
answer_list.append(numbers[answer])
while prev[answer] != -1:
    answer = prev[answer]
    answer_list.append(numbers[answer])
answer_list.reverse()
for i in answer_list:
    print(i, end = ' ')
#4 8 2 6 2 10 6 29 30 58 9