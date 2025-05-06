import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados do CSV
df = pd.read_csv('California Wildfire Damage.csv')

cores = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f']

# Ordenando os dados por Área queimada e Casas destruídas
sorteados = df.sort_values(by='Area_Burned (Acres)', ascending=False)
ord = df.sort_values(by='Homes_Destroyed', ascending=False)

# Gráfico 1: Áreas queimadas
plt.figure(figsize=(10,6))
plt.barh(sorteados['Location'][:8], sorteados['Area_Burned (Acres)'][:8], label='Áreas queimadas',color = 'purple')
plt.title("Áreas Queimadas")
plt.xlabel('Áreas (Acres)')
plt.ylabel('Localizações')
plt.tight_layout()
plt.show()

# Gráficos 2 e 3: Casas destruídas e Empresas destruídas
fig, ax = plt.subplots(1, 2, figsize=(10,6))

# Casas destruídas
ax[0].bar(ord['Location'][:8], ord['Homes_Destroyed'][:8],color = 'green')
ax[0].set_title('Casas destruídas por país')
ax[0].tick_params(axis='x', rotation=45)

# Empresas destruídas
ax[1].bar(ord['Location'][:8], ord['Businesses_Destroyed'][:8],color = 'green')
ax[1].set_title('Empresas destruídas por país')
ax[1].tick_params(axis='x', rotation=45)  # Rot_

plt.tight_layout()
plt.show()