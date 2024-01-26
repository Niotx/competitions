t = int(input())

answer = []
for _ in range(t):
    n = int(input())
    matrixA = []
    for _ in range(n):
        element = input()
        arrA = element.split()
        arrA = list(map(int, arrA))
        matrixA.append(arrA)
    matrixB = []
    for _ in range(n):
        element = input()
        arrB = element.split()
        arrB = list(map(int, arrB))
        matrixB.append(arrB)
    matrixF =[]
    #for i in range(n):
    for j in range(n):
        for _ in range(n):
            if matrixB[_] == matrixA[j]:
                matrixF[j] = matrixB[_]
            else:
                matrixF[_][_+1] = matrixB[_][_+1]

    if matrixA == matrixF:
        print("YES")
    else:
        print("NO")
        print(matrixF)
