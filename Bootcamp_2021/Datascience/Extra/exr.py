N = int(input())
dna = list(input().split())
M = int(input())

for i in range(0,N,M):
    print("".join(dna[i:i+M]),end=" ")