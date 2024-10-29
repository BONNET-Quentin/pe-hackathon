# # Étude de l'influence des étoiles entourant une exoplanète



import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('données.csv', sep=';')
sns.set_style('darkgrid')

# ## On s'intéresse d'abord au lien entre température et nombre d'étoiles

# L'idée est ici de voir s'il est intéressant de chercher une planète avec 1 seule étoile pour que la température en surface reste assez faible, ou si au contraire il est plus avantageux pour avoir uen température d'équilibre viable d'avoir plusieurs étoiles. 

dh= pd.read_csv('données.csv', sep=';').dropna(subset=['pl_eqt', 'Nombre_etoile'])
sns.relplot(data=dh, x='Nombre_etoile', y='pl_eqt');

# On voit ici qu'il n'y a pas de corrélation ! :(
# En effet, en faisant abstraction du fait qu'il y a moins de planètes possédant 2 et surtout 3 étoiles, on voit que toutes les gammes de températures moyennes peuvent être atteintes même avec une seule étoile : ce critère n'est a priori pas discriminant pour trouver une planète viable. 

# ## On regarde maintenant s'il y a un lien même entre la luminosité reçue et la température moyenne

# En effet, une décorrélation trop marquée entre luminosité reçue et température tendrait à montrer une composition particulière de la planète, voire la présence de l'eau. 
# La chaleur finalement absorbée dépend en effet directement de la structure de la planète, et ces informations sont donc intéressantes pour la viabilité de la planète.
# On trie les informations en fonction du nombre d'étoiles entourant les planètes.

df=df.dropna(subset=['pl_eqt', 'Nombre_etoile','Luminosité'])



sns.relplot(data=df, x='Luminosité', y='pl_eqt', hue='Nombre_etoile', col='Nombre_etoile');
sns.relplot(data=df, x='Luminosité', y='pl_eqt', hue='Nombre_etoile');

# On observe bien une forme de corrélation : la température semble effectivement être fonction croissante de la luminosité (celle ci étant négative à cause de la formule mettant en jeu des logarithmes).
# Le nombre d'étoiles n'a pas d'influence a priori. 
#

# ## Finalement on regarde le lien entre température et insolation

# On veut voir de même s'il y a un lien avec l'insolation et la température.

dg= pd.read_csv('données.csv', sep=';').dropna(subset=['pl_eqt', 'Insolation'])

dg.sort_values(by=['pl_eqt'])
sns.relplot(data=dg, x='Insolation', y='pl_eqt', hue='Nombre_etoile');

# On observe effectivement un lien direct entre température et insolation, en notant que la courbe est similaire à celle de luminosité/température. 
# La plupart des planètes ont une insolation assez faible, proche de celle de la Terre, ce qui peut sembler avantageux. 


