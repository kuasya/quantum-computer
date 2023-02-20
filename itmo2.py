
# Этап 2

def apply_evolution(k, operator, state):
    state_new = [0 for i in range(2 ** k)]

    for j in range(2**k):
        for i in range(2**k):
            state_new[j] += operator[i][j] * state[j]
    return state_new


a, b = input().split()

k = int(a)
state = [float(i) for i in input().split()]
operator = [[0]*(2**k) for i in range(2**k)]

for i in range(2**k):
    operator[i] = [int(j) for j in input().split()]

# print(a, b)
# print(state)
# print(operator)

state_new = apply_evolution(k, operator, state)
for i in range(len(state_new)):
    if i != 2**k - 1:
        print(state_new[i], end=' ')
    else:
        print(state_new[i])


maska = [int(i) for i in b]
p = maska.count(0)
vector = [0 for i in range(2**(k-p))]

# print(vector)
