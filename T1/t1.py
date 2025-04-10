'''
Exercício 01

    Desenvolva um algoritmo que seja capaz de resolver um sistema de equações lineares abaixo

        y = 0.5x + 0.5
        y = −x + 2

    Como resultado, sua saída devera apresentar o resultado do sistema de equações e plotar as equações, o ponto x,y

'''

import numpy as np
import matplotlib.pyplot as plt

# Ax = B
A = np.array([[0.5, -1], [1, 1]])
B = np.array([-0.5, 2])

# interseção
solucao = np.linalg.solve(A, B)
x_intersecao, y_intersecao = solucao
print(f'O ponto de interseção é: x = {x_intersecao}, y = {y_intersecao}')

# desenhar grafico equação
x = np.linspace(-1, 4, 100)

# equações
y1 = 0.5 * x +0.5
y2 = -x + 2
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label='y = 0.5x + 0.5'. color='blue')
plt.plot(x, y2, label='y = -x + 2', color='red')

# ponto interseção
plt.scatter(x_intersecao, y_intersecao, color='purple,' zorder=5)
plt.text(x_intersecao, y_intersecao, f'({x_intersecao:.2f}, {y_intersecao:.2f})', fontsize=9, ha='left', va='bottom')

