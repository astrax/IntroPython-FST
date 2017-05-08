import numpy as np
import matplotlib.pyplot as plt

# Essayez de reproduire la figure indiquée dans images/exercise_Mpl1.png

# Nos données ...
x = np.linspace(0, 10, 100)
y1, y2, y3 = np.cos(x), np.cos(x + 1), np.cos(x + 2)
titres = ['Signal 1', 'Signal 2', 'Signal 3']
fig, axes = plt.subplots(nrows=3)
fig.tight_layout() #Ajuster en sorte que les subplots remplissent la figure

# Pouvez-vous comprendre ce qu'il faut faire ensuite 
#pour tracer x vs y1, y2 et y3 sur une figure?
