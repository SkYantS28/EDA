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
plt.plot(x, y1, label='y = 0.5x + 0.5', color='blue')
plt.plot(x, y2, label='y = -x + 2', color='red')

# ponto interseção
plt.scatter(x_intersecao, y_intersecao, color='purple', zorder=5)
plt.text(x_intersecao, y_intersecao, f'({x_intersecao:.2f}, {y_intersecao:.2f})', fontsize=9, ha='left', va='bottom')

# organizar
plt.title('Sistema de Equações Lineares')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.show()

'''
erro:
  File "c:\Users\Sky Crizosti\OneDrive\Desktop\faculdade\quarto_periodo\estrutura_algoritmo_avançado\T1\t1.py", line 32
    plt.plot(x, y1, label='y = 0.5x + 0.5'. color='blue')
                                                 ^
SyntaxError: invalid syntax
PS C:\Users\Sky Crizosti\OneDrive\Desktop\faculdade\quarto_periodo\estrutura_algoritmo_avançado> 
'''
            
'''
novo erro:
  File "c:\Users\Sky Crizosti\OneDrive\Desktop\faculdade\quarto_periodo\estrutura_algoritmo_avançado\T1\t1.py", line 36
    plt.scatter(x_intersecao, y_intersecao, color='purple,' zorder=5)
                                                  ^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
PS C:\Users\Sky Crizosti\OneDrive\Desktop\faculdade\quarto_periodo\estrutura_algoritmo_avançado> 
'''
