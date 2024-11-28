a = b = c = xm = xn = d = r = dn = float
a = float(input("Digite o valor de a: "))


b = float(input("Digite o valor de b: "))


c= float(input("Digite o valor de c: "))


d = ((b*b)-(4*a*c))
print("Delta: ", d)
if d < 0:
    dn = -(d)
    d = dn
    r = (type(RaizQ)) (d)  # type: ignore
    print("Raiz de Delta é: ", r)
    xm = ((-b + r )) / (2*a)



    print("O valor de X1 è: ",xm,"!")


    xn = ((-b - (r))/ (2*a))
    ("O valor de x'' é: ",xn, "!")
else:
    r = (type(RaizQ)) (d) # type: ignore
    print("Raiz de Delta: ",r)
    xm = ((-b + (r)) /(2*a))


    print("O valor de X' é: ",xm)


    xn = ((-b - (r)) /(2*a))


    print("O valor de X'' é: ",xn)