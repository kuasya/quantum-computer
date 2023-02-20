Q = list(map(float, input().split()))
V = list(map(float, input().split()))
Y = list(map(float, input().split()))

# for i in range(2):
#     for j in range(2):
#         V[i][j] = [[float(x)] for x in input().split()]

Vt = [V[0], V[2], V[1], V[3]]
T = []
# print(Vt)

for i in range(0,3,2):
    for j in range(0,2):
        T += [Y[i] * Vt[j] + Y[i+1] * Vt[j+2]]
# print(T)
#
# for i in range(2):
#     for j in range(2):
#         T += []

Qt = [Q[0], Q[2], Q[1], Q[3]]
# print(Qt)

W = []
for i in range(0,3,2):
    for j in range(0,2):
        W += [Qt[i] * T[j] + Qt[i+1] * T[j+2]]

for i in range(3):
    print(W[i], end = ' ')
print(W[3])



