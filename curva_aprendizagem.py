import matplotlib.pyplot as plt
import numpy as np

# Faixas etárias ajustadas de 12 a 80 anos
age_groups = ['12-18', '19-25', '26-35', '36-50', '51-65', '66-80']

# Dados simulados para níveis de proficiência por faixa etária ao longo do tempo (em horas)
proficiency_levels = {
    '12-18': [95, 97, 98, 99, 100, 100, 100],  # Jovens altamente adaptáveis
    '19-25': [90, 92, 94, 97, 98, 99, 100],    # Jovens adultos adaptáveis
    '26-35': [80, 85, 88, 92, 95, 98, 100],    # Adultos com bom aprendizado
    '36-50': [70, 75, 80, 85, 88, 92, 95],     # Aprendizado moderado
    '51-65': [60, 65, 70, 75, 80, 85, 88],     # Aprendizado gradual
    '66-80': [50, 55, 60, 65, 70, 75, 80],     # Desafios maiores na adaptação
}

# Tempo dedicado ao aprendizado (em horas, assumindo 30 horas por "mês")
time_spent_hours = [30, 60, 90, 120, 150, 180, 210]  # 7 períodos de 30 horas cada

# Criando o gráfico
plt.figure(figsize=(12, 8))

# Plotando as curvas de cada faixa etária
for age_group in age_groups:
    plt.plot(time_spent_hours, proficiency_levels[age_group], marker='o', label=f'Idade {age_group}')

# Configurações do gráfico
plt.xlabel('Tempo Dedicado ao Aprendizado (horas)')
plt.ylabel('Nível de Proficiência Alcançado (%)')
plt.title('Curva de Aprendizagem de Novas Tecnologias por Faixa Etária (12 a 80 anos)')
plt.xticks(time_spent_hours)  # Marcar pontos no eixo X com as horas
plt.legend()
plt.grid(True)

# Exibindo o gráfico
plt.show()
