def conta_vogais(str):
    str = str.lower()
    vogais = 'aeiou'
    return {i:str.count(i) for i in vogais if i in str}
print(conta_vogais("olaaa"))