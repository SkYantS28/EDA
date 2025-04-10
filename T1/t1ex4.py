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
