n = int(input())
in_list = list(map(int, input().split()))

visit = [False] * n
answer = 0

def sol(li):
    global answer
    if len(li) == n:
        total = 0
        for i in range(n+1):
            total += abs(li[i] - li[i+1])
        answer = max(answer, total)
        return

    for i in range(n):
        if not visit[i]:
            visit[i] = True
            li.append(in_list[i])
            sol(li)
            visit[i] = False
            li.pop()


sol([])
print(answer)
