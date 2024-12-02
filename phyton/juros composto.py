vi = float(input("Valor inicial: "))
i=float(input("Rentabilidade mensal: "))

i = i / 100

m= int(input("Meses que vai deixar rendendo: "))
vf= vi * (1+i) **m

print("Valor após",m,"meses: R$",vf)
