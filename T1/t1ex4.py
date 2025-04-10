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
