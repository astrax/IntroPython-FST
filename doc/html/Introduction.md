
# Introduction à la programmation scientifique
<span style="color:blue; font-family:Georgia; font-size:1.5em;">Ahmed Ammar et Hassen Ghalila</span>

<span style="color:blue; font-family:Georgia; font-size:1em;">Faculté des Sciences de Tunis, Université de Tunis El Manar</span>


```python
#Juste pour savoir la dernière fois que cela a été exécuté:
import time
print(time.ctime())
```

    Mon May  8 02:05:43 2017


## Langage Python


[Python] (http://www.python.org/) est un langage de programmation moderne de haut niveau, orienté objet et d'usage général.

Caractéristiques générales de Python:

* ** Langage simple: ** facile à lire et à apprendre avec une syntaxe minimaliste.
* ** Langage concis et expressif: ** moins de lignes de code, moins de bugs, plus facile à maintenir.

Détails techniques:

* ** Typé dynamiquement: ** Pas besoin de définir le type des variables, les arguments ou le type des fonctions.
* ** La gestion automatique de la mémoire: ** Aucune nécessité d'allouer explicitement et désallouer la mémoire pour les variables et les tableaux de données. Aucun bug de fuite de mémoire.
* ** Interprété: ** Pas besoin de compiler le code. L'interpréteur Python lit et exécute le code python directement.

### Avantages:

* Le principal avantage est la facilité de programmation, qui minimise le temps nécessaire pour développer, déboguer et maintenir le code.
* Langage bien conçu qui encouragent les bonnes pratiques de programmation:
  * Modulaire et orientée objet, permet l'encapsulation  et la réutilisation de code. Il en résulte souvent un code plus transparent, maintenable et sans bug.
  * Documentation intégré avec le code.
* De nombreuses bibliothèques standards, et de nombreux packages add-on.

### Inconvénients:

* Puisque Python est un langage de programmation interprété et typé dynamiquement, l'exécution de code python peut être lent par rapport à des langages de programmation compilés à typage statique, tels que C et Fortran.
* Un peu trop décentralisé, avec différents environnements, bibliothéques, et documentation répartis à différents endroits. Cela peut le rendre difficile pour commencer.


## Installation d'un environnement Python scientifique

[Anaconda CE](http://continuum.io/downloads.html). Anaconda Community Edition is free.

## Documents et sites Web sur Python

* [Python](http://www.python.org). The official Python web site.
* [Python tutorials](https://docs.python.org/3.6/tutorial/). The official Python tutorials.
* [Think Python](http://www.greenteapress.com/thinkpython). ''How to Think Like a Computer Scientist'' by Allen B. Downey (free book).
* [Python Course](http://python-course.eu/python3_course.php). This website contains a free and extensive online tutorial by Bernd Klein, well suited for self-learning. However, you can attend one of his Python courses in Paris, London, Toronto, Berlin, Frankfurt, Hamburg Munich or Lake Constance. 

## Cours sur github:
- ["Scientific Python Lectures"](https://github.com/jrjohansson/scientific-python-lectures) by  Robert Johansson
- ["Anatomy Of Matplotlib"](https://github.com/WeatherGod/AnatomyOfMatplotlib) by  Benjamin Root
- ["Python-lectures-Notebooks"](https://github.com/Morisset/Python-lectures-Notebooks) by Christophe Morisset

## Version de Python et bibliothéques utilisées


```python
print ("\t\tSystème utilisé")
import sys
print("Système :\t\t",sys.platform)
import platform
print(platform.platform())
print("Ordinateur:\t\t",platform.machine())
print("Version de Python:\t",sys.version)
import IPython
print("Version de IPython:\t",IPython.__version__)
import numpy
print("Version de numpy:\t",numpy.version.version)
import scipy
print("Version de scipy:\t",scipy.version.version)
import matplotlib
print("Version de matplotlib:\t",matplotlib.__version__)
```

    		Système utilisé
    Système :		 linux
    Linux-4.8.0-51-generic-x86_64-with-debian-stretch-sid
    Ordinateur:		 x86_64
    Version de Python:	 3.6.0 |Anaconda custom (64-bit)| (default, Dec 23 2016, 12:22:00) 
    [GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]
    Version de IPython:	 5.1.0
    Version de numpy:	 1.11.3
    Version de scipy:	 0.18.1
    Version de matplotlib:	 2.0.0

