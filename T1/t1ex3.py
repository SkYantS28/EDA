'''
Exercícios 03

    Encontrando um ponto dentro de uma Função
    N|Solid

    Como engenheiro de software voce recebeu a missão de encontrar o valor aproximado de ( x ) que faz com que uma determinada função ( f(x) ) seja igual a zero.

    Para isso, como explicado nas aulas anteriores você sabe que o valor deverá ser investigado dentro de um intervalo ([a, b]), onde:

    ( f(a) ) e ( f(b) ) possuem sinais opostos (um é positivo e o outro é negativo).

    O seu objetivo é criar um algoritmo que, a cada etapa, reduza esse intervalo até obter um valor de ( x ) com um erro aceitável.

    Passos:
        Escolha um ponto médio ( m ) entre ( a ) e ( b ).

        Avalie ( f(m) ).

        Se ( f(m) ) for suficientemente próximo de zero, pare. Caso contrário:
        
            Se ( f(m) ) e ( f(a) ) tiverem sinais opostos, então a raiz está entre ( a ) e ( m ), e você deve descartar ( b ).

            Caso contrário, o valor de interesse está entre ( m ) e ( b ), e você deve descartar ( a ).

        Repita o processo até atingir a precisão desejada.

        Aplique esse método para encontrar este ponto na função:

            [ f(x) = x^3 - x - 2 ]

        no intervalo ([1, 2]) com uma precisão de ( 10^{-4} ).
'''

# definir função p encontarr
def f(x):
    return (x ** 3) - x - 2

# função implementar metodo bisseção p encontrar raiz
def bissecao(a, b, precisao):
    if f(a) * f(b) >= 0: #verifica se sinais são opostos
        print("O m´rtodo de bissesão não pode ser aplicado, pois f(a) e f(b) devem ter sinais opostos.")
        return None
    
    # loop divide intevalo a,b ate precisao desejada ser atingida
    while (b - a) / 2 > precisao:
        m = (a + b) / 2 #ponto medio
        if f(m) == 0:
            break #achou raiz exata, sai do loop
        elif f(a) * f(m) < 0:
            b = m # se for negativo, a razis esta entre 'a' e 'm'
        else:
            a = m #senão, raiz esta entre 'm' e 'b'
    return (a + b) / 2 #retornna media entre 'a' e 'b' fomo raiz aprox

# definir intervalo 'a,b / precisão desejada para o calculo da raiz
a = 1
b = 2
precisao = 1e-4 #1×10^−4, ou seja, o número 0.0001

# chamar função bissecao com os valores definidos
raiz = bissecao(a, b, precisao)
print(f"A raiz aproximada é: {round(raiz, 2)}")

'''
terminal:
A raiz aproximada é: 1.52
PS C:\Users\Sky Crizosti\OneDrive\Desktop\faculdade\quarto_periodo\estrutura_algoritmo_avançado> 
'''
