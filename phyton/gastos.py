gastos_angelo = [300, 500, 200, 800]
gastos_leandra = [200, 300, 500, 700]

total_gastos_angelo = sum(gastos_angelo)
total_gastos_leandra = sum(gastos_leandra)

if total_gastos_angelo > total_gastos_leandra:
    print("Angelo gastou mais esse mês")
elif total_gastos_leandra > total_gastos_angelo:
    ("Angelo e Leandra gastaram a mesma quantia esse mês")
