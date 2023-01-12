import random
import sys

import numpy



f = open("adj_matrix.txt", "r")

length = int(f.readline())
mat = [[0 for c in range(length)] for r in range(length)]

for index, line in enumerate(f):
    lines = line.split()
    for idx, element in enumerate(lines):
        element = int(element)
        mat[index][idx] = element


#MonteCarlo Method
print("input: ")
input = sys.stdin.readline()
inputs = input.split(",")
N = int(inputs[0])
S = int(inputs[1])
E = float(inputs[2])


A = []
visiter = [0 for c in range(length)]

rand1 = N
rand2 = N
for i in range(S):

    prob = numpy.random.random(1)

    if prob > E:

        for idx, num in enumerate(mat):
            if mat[rand1][idx] == 1:
                A.append(idx)
        rand2 = A[random.randint(0, len(A) - 1)]
        visiter[rand2] += 1
        rand1 = rand2

    else:
        visiter[N] += 1
        rand1 = N


    A = []


sorted = [[0 for c in range(2)] for r in range(len(visiter))]

for idx, v in enumerate(visiter):
    sorted[idx] = [idx,v]

sorted = numpy.array(sorted)

sorted = numpy.flip(sorted[sorted[:, 1].argsort()])
sorted = sorted[:10]

print("node     score     node type")
for score, node in sorted:
    if N == node:
        print("{:<9}{:<10}{:<9}".format(node, score/S, "node N"))
    elif mat[N][node] == 1:
        print("{:<9}{:<10}{:<9}".format(node, score/S, "current friend"))
    else:
        print("{:<9}{:<10}{:<9}".format(node, score/S, "recommended friend"))



