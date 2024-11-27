faturamento = 1200
custo = 700
lucro = faturamento - custo
margem_lucro = lucro / faturamento

print("Faturamento da empresa: R$", faturamento)
print(f"Faturamento da empresa: R${faturamento:.2f} Custo: R$ {custo:.2f} Lucro: R$ {lucro:.2f}")

email_cliente = "angelo@gmail.com"

# Maiusculas
email_cliente = email_cliente.upper()
print(email_cliente)

# Minusculas
email_cliente = email_cliente.lower()
print(email_cliente)
# Encontrar o @ ou outros caracteres quaisquer
print(email_cliente.find("@"))

#Tamanho do texto
print(len((email_cliente)))

#Pegar um caracter
print(email_cliente[3])
print(email_cliente[-4])

#Pegar um pedaço de texto
print(email_cliente[:6])
print(email_cliente[6:])
print(email_cliente[3:10])

#Tocar um pedaço do texto
novo_email = email_cliente. replace("gmail.com", "yahoo.com.br")
print(email_cliente)
print(novo_email)

nome = "angelo gabriel silva de camargo"

print(nome.capitalize())
print(nome.title())
print(nome.upper())

#Pegar o servidor do email
posicao_arroba = email_cliente.find("@") + 1
servidor = email_cliente[posicao_arroba:]
print(servidor)

# Pegar o primeiro nome 
posicao_espaco = nome.find(" ")
primeiro_nome = nome[:posicao_espaco].title()
print(primeiro_nome)

# Pegar o sobrenome
sobrenome = nome[posicao_espaco + 1:].title()
print(sobrenome)

print(f"Faturamento da empresa: R${faturamento:.2f} Custo: R$ {custo:.2f} Lucro: R$ {lucro:.2f} Margem: {margem_lucro: .0%}")
