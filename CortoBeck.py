# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---



# pe-hackathon

# +

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -



# On étudie en particulier la luminosité apparente et la température moyenne des planètes en fonction de différents paramètres de la table de données. 

df=pd.read_csv('données.csv',delimiter=';')
df.head(5)

# +
df1 = df.dropna(subset=['Luminosité','Nombre_etoile'])
plt.figure(figsize=(10, 6))
plt.scatter(df1['Nombre_etoile'], df1['Luminosité'], color='r', marker='o')
plt.style.use("cyberpunk")
plt.xlabel('Nombre d\'étoiles')
plt.ylabel('Luminosité apparente')
plt.title('Luminosité en fonction du Nombre d\'étoiles')
mplcyberpunk.add_glow_effects()

plt.show()

# +
df2 = df.dropna(subset=['Luminosité','Distance'])
plt.figure(figsize=(10, 6))
plt.scatter(df2['Distance'], df2['Luminosité'], color='r', marker='o')
plt.xlabel('Distance [pc]')
plt.ylabel('Luminosité apparente')
plt.title('Luminosité en fonction de la distance')
plt.style.use("cyberpunk")
mplcyberpunk.add_glow_effects()


plt.show()

# +
df3 = df.dropna(subset=['Luminosité','Eccentricité'])
plt.figure(figsize=(10, 6))
plt.scatter(df3['Eccentricité'], df3['Luminosité'], color='r', marker='o')
plt.xlabel('Eccentricité')
plt.ylabel('Luminosité apparente')
plt.title('Luminosité en fonction de l\'eccentricité')
plt.style.use("cyberpunk")
mplcyberpunk.add_glow_effects()


plt.show()

# +
df4 = df.dropna(subset=['Nombre_etoile', 'Luminosité', 'Distance'])

plt.style.use('dark_background')

plt.figure(figsize=(10, 6))
scatter = plt.scatter(df4['Distance'], df4['Luminosité'], 
                      c=df4['Nombre_etoile'], cmap='viridis', marker='o', alpha=0.7,s=10)

cbar = plt.colorbar(scatter)
cbar.set_label("Nombre d'étoiles")

plt.xlabel('Distance')
plt.ylabel('Luminosité')
plt.title('Luminosité en fonction de la distance')

plt.show()



# +
df5 = df.dropna(subset=['Nombre_etoile', 'Luminosité', 'Distance'])


plt.style.use('dark_background')

# Créer une palette de couleurs discrète
unique_values = df5['Nombre_etoile'].unique()
cmap = plt.get_cmap('tab10', len(unique_values)) 

plt.figure(figsize=(10, 6))
scatter = plt.scatter(df5['Distance'], df5['Luminosité'], 
                      c=df5['Nombre_etoile'], cmap=cmap, marker='o', alpha=0.7, s=2)  

# Ajouter une barre de couleur discrète pour indiquer le 'Nombre_etoile'
cbar = plt.colorbar(scatter, ticks=range(len(unique_values)))
cbar.set_label("Nombre d'étoiles")
cbar.set_ticks(unique_values) 
cbar.set_ticklabels(unique_values)


plt.xlabel('Distance [pc]')
plt.ylabel('Luminosité apparente')
plt.title('Luminosité en fonction de la Distance avec variation discrète du Nombre d\'étoiles')


plt.show()


# +
df6 = df.dropna(subset=['Nombre_etoile', 'pl_eqt', 'Insolation'])


plt.style.use('dark_background')

# Créer une palette de couleurs discrète
unique_values = df6['Nombre_etoile'].unique()
#cmap = plt.get_cmap('tab10', len(unique_values)) 
cmap = plt.get_cmap('Set1', 3)

plt.figure(figsize=(10, 6))
scatter = plt.scatter(df6['Insolation'], df6['pl_eqt'], 
                      c=df6['Nombre_etoile'], cmap=cmap, marker='o', alpha=0.7, s=5)  

# Ajouter une barre de couleur discrète pour indiquer le 'Nombre_etoile'
cbar = plt.colorbar(scatter, ticks=range(len(unique_values)))
cbar.set_label("Nombre d'étoiles")
cbar.set_ticks(unique_values) 
cbar.set_ticklabels(unique_values)


plt.xlabel('Insolation [Earth Flux]')
plt.ylabel('Température [K]')
plt.title('Température en fonction de l\'insolation avec variation discrète du Nombre d\'étoiles')


plt.show()


# +

df7 = df.dropna(subset=['pl_eqt'])

plt.style.use('dark_background')

bin_width = 5 
min_temp = df7['pl_eqt'].min() 
max_temp = df7['pl_eqt'].max()  
bins = range(int(min_temp), int(max_temp) + bin_width, bin_width) 

plt.figure(figsize=(10, 6))
plt.hist(df7['pl_eqt'], bins=bins, color='cyan', edgecolor='red', alpha=0.7)

plt.xlabel('Température (K)')
plt.ylabel('Nombre de planètes')
plt.title('Nombre de planètes par intervalle de température de 5K')

plt.show()
# -

df8=df.dropna(subset=['pl_eqt'])
masque_temperature = (df8['pl_eqt'] >= 273) & (df8['pl_eqt'] <= 303)
df8_filtre = df8[masque_temperature]
print(df8_filtre.head(20))

