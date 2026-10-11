n = int(input("Введіть N: "))

A = [[0 for _ in range(n)] for _ in range(3)]

for i in range(n):
    A[0][i] = 1 + 2 * i


for i in range(n):
    A[1][i] = 5 + 4 * i

for i in range(n):
    A[2][i] = 21 + i

B = [0 for _ in range(n)]

for i in range(n):
    B[i] = A[0][i] + A[1][i] + A[2][i]

print("Матриця A:")
for row in A:
    print(row)

print("Масив B:")
print(B)
