
A = []
B = []


for i in range(10):
    num_a = int(input(f"Digite o {i+1}º número para o vetor A: "))
    A.append(num_a)


for i in range(10):
    num_b = int(input(f"Digite o {i+1}º número para o vetor B: "))
    B.append(num_b)


C = []
for i in range(10):
    C.append(A[i])  
    C.append(B[i])  


print("\nVetor C (intercalado):")
print(C)
