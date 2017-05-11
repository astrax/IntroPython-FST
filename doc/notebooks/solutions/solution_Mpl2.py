import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1)

# Générer des données aléatoires avec différentes plages ...
data1 = np.random.random((10, 10))
data2 = 2 * np.random.random((10, 10))
data3 = 3 * np.random.random((10, 10))

# Configurer la figure et les axes ...
fig, axes = plt.subplots(ncols=3, figsize=plt.figaspect(0.5))
fig.tight_layout() #Ajuster en sorte que les subplots remplissent la figure
cax = fig.add_axes([0.25, 0.1, 0.55, 0.03]) # Ajouter un axe pour la barre de couleurs

# Maintenant, vous êtes tout seul!
for ax, data in zip(axes, [data1, data2, data3]):
    im = ax.imshow(data, vmin=0, vmax=3, interpolation='nearest')

fig.colorbar(im, cax=cax, orientation='horizontal')
plt.show()
