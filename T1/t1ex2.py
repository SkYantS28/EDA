'''
Exercício 02

    O problema que usaremos é bem conhecido e bastante simples.
    
    Queremos resolver uma equação de segundo grau, ou seja, dada a equação :

        𝒂𝒙𝟐 + 𝒃𝒙 + 𝒄,

    queremos saber quais são as suas raízes reais, se elas existirem.
    
    Desta forma, resolva a função 2𝑥ˆ2 + 2𝑥 − 6.
'''

# coeficiente da equaç~~ao
a = 2
b = 2
c = -6

# calcular delta
#b^2 - 4ac
delta = (b ** 2) - 4 * a * c

# existe raiz real?
if delta < 0:
    print(f'A equação 2𝑥ˆ2 + 2𝑥 − 6, não possui raízes reais. Pois o valor de seu delta é: {delta}. Sendo inferior a zero.')
else:
    # calcular raizes reais
    # -b + delta ** 0.5) / (2 * a)
    r1 = (-b + delta ** 0.5) / (2 * a)
    r2 = (-b - delta ** 0.5) / (2 * a)
    
    # resultado
    print("Raiz 1:", r1)
    print("Raiz 2:", r2)
