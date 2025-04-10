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