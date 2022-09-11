l = []

def route(n):
    l.append(n)
    if n == 1:
        l.reverse()
        print(l)
        l.reverse()
        return

    for i in range(len(father[n])):
        route(father[n][i])
        l.pop()
    return

n = int(input('Enter the Number of Vertexes: '))
m = int(input('Enter the Number of Edges: '))
mat = [[-1] * (n + 1) for i in range(n + 1)]

cost = [10000] * (n + 1)
father = [[] for i in range(n + 1)]

for i in range(m):
    v1 = int(input())
    v2 = int(input())
    k = int(input())
    mat[v1][v2] = k

cost[1] = 0
father[1] = [1]

for i in range(n):
    for j in range(n + 1):
        if (mat[i][j] != -1) and (cost[i] + mat[i][j] < cost[j]):
            cost[j] = cost[i] + mat[i][j]
            father[j] = []
            father[j].append(i)
            print(i, j, cost[j])
        elif (mat[i][j] != -1) and (cost[i] + mat[i][j] == cost[j]):
            father[j].append(i)

route(n)
print(f'Cost: {cost.pop()}')
