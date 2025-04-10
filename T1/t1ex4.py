'''
Exercícios 04

    Um engenheiro de automação capturou durante um período de 30 dias Dados Climáticos, diversos valores de temperatura, umidade e pressão de um ambiente específico.
    
    Sabendo que o acumulado de 24 horas foi a resultante de aporte de n ciclos de 10 minutos, calcule:

        Para todas as grandezas climáticas, os valores mínimos, máximos, médios em 24 horas de um do vigésimo dia;
        
        A quantidade de ciclos por período de coleta neste dia.

'''
import numpy as np

# definir número de dias e ciclos
dias = 30
ciclos_por_dia = (24 * 60) // 10  # 24h divididas em ciclos de 10 minutos


# gerar dados fictícios para temperatura, umidade e pressão
np.random.seed(42)  # resultados sejam reproduzíveis

#criar arrays(listas) de dados aleatórios para cada grandeza climática para 30 dias
temperatura = np.random.uniform(18, 35, (dias, ciclos_por_dia))
umidade = np.random.uniform(30, 90, (dias, ciclos_por_dia))
pressao = np.random.uniform(980, 1030, (dias, ciclos_por_dia))

# definir dia de interesse (vigésimo dia)
dia_interesse = 19  #índice é 19 porque começa de 0

# obter os dados do vigésimo dia
temperatura_dia_20 = temperatura[dia_interesse]
umidade_dia_20 = umidade[dia_interesse]
pressao_dia_20 = pressao[dia_interesse]

# calcular valores min, max e médios
min_temp = np.min(temperatura_dia_20)
max_temp = np.max(temperatura_dia_20)
media_temp = np.mean(temperatura_dia_20)

min_umidade = np.min(umidade_dia_20)
max_umidade = np.max(umidade_dia_20)
media_umidade = np.mean(umidade_dia_20)

min_pressao = np.min(pressao_dia_20)
max_pressao = np.max(pressao_dia_20)
media_pressao = np.mean(pressao_dia_20)


#resultados
print(f"Para o dia 20 (índice 19):")
print(f"Temperatura - Min: {min_temp:.2f}°C, Max: {max_temp:.2f}°C, Média: {media_temp:.2f}°C")
print(f"Umidade - Min: {min_umidade:.2f}%, Max: {max_umidade:.2f}%, Média: {media_umidade:.2f}%")
print(f"Pressão - Min: {min_pressao:.2f} hPa, Max: {max_pressao:.2f} hPa, Média: {media_pressao:.2f} hPa")
print(f"Quantidade de ciclos por período de coleta no dia 20: {ciclos_por_dia}")
'''
terminal
Para o dia 20 (índice 19):
Temperatura - Min: 18.13°C, Max: 34.91°C, Média: 26.65°C
Umidade - Min: 30.55%, Max: 89.50%, Média: 60.88%
Pressão - Min: 980.39 hPa, Max: 1029.97 hPa, Média: 1004.96 hPa
Quantidade de ciclos por período de coleta no dia 20: 144
PS C:\Users\Sky Crizosti\OneDrive\Desktop\faculdade\quarto_periodo\estrutura_algoritmo_avançado>
'''
