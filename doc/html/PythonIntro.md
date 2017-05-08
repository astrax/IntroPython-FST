
# Introduction à Python
<span style="color:blue; font-family:Georgia; font-size:1.5em;">Ahmed Ammar et Hassen Ghalila</span>

<span style="color:blue; font-family:Georgia; font-size:1em;">Faculté des Sciences de Tunis, Université de Tunis El Manar</span>


```python
#Juste pour savoir la dernière fois que cela a été exécuté:
import time
print(time.ctime())
```

## Utilisation de Python comme calculatrice

L'utilisation de la fonction `print()` n'est pas nécessaire pour obtenir un résultat. Il suffit de taper certaines opérations et le résultat est obtenu avec les touches `<SHIFT> + <ENTRER>`.


```python
2 + 22
```


```python
(2+3)*(3+4)/(5*5)
```

Python aime l'utilisation des espaces pour rendre les scripts plus lisibles


```python
(2+3) * (3+4.) / (5*5)
```

L'art d'écrire un bon code python est décrit dans le document suivant: http://legacy.python.org/dev/peps/pep-0008/

## Affectations

Comme tout autre langage de programmation, vous pouvez affecter une valeur à une variable. Ceci est fait avec le symbole "="


```python
a = 4
```


```python
a
```


```python
a = a + 1
a
```


```python
a *= 4 # semblable à a = a * 4
a
```


```python
a, b = 1, 3
a, b
```

Certains noms de variables ne sont pas disponibles, ils sont réservés à python lui-même:

and, as, assert, break, class, continue, def, del, elif, else, except, 
exec, finally, for, from, global, if, import, in, is, lambda, not, or,
pass, print, raise, return, try, while, with, yield


```python
lambda_ = 2
file = 3
```

## Les commentaires


```python
a = 2 # ceci est un commentaire
```


```python
"""C'est un grand commentaire
sur plusieurs lignes
la fin est comme il a commencé"""
```

## Les types

Les types utilisés dans Python sont:integers, long integers, floats (double prec.), complexes, strings, booleans.

La fonction `type()` donne le type de son argument:


```python
type(2)
```


```python
type(2.3)
```


```python
int(0.8) # Tronquer
```


```python
round(0.8765566777) # Valeur la plus proche
```


```python
a = 1.5 + 0.5j # Nombres complexes
```


```python
a**2.
```


```python
(1+2j)*(1-2j)
```


```python
a.real
```


```python
(a**3).imag
```


```python
a.conjugate() # C'est une fonction, il faut ()
```

### Booleans

Les opérateurs de comparaison sont: <, >, <=, >=, ==, !=


```python
5 < 7
```


```python
a = 5
b = 7
```


```python
b < a
```


```python
c = 2
```


```python
c < a < b
```


```python
a < b and b < c
```


```python
res = a < 7
print(res, type(res))
```


```python
print (int(res))
```


```python
not res is True
```


```python
a = True
print (a)
```

## Formatage des chaînes


```python
print("Hello world!")
```


```python
print ('Hello world!')
```


```python
print ("Hello I'm here") # ' à l'intérieur ""
```


```python
# C'est l'ancien mode de mise en forme des sorties (style C)
a = 7.5
b = 'tralala'
c = 8.9e-33
print('a = %f, b = %s, c = %e' % (a, b, c))
```


```python
# La nouvelle façon est d'utiliser la méthode format() de l'objet chaîne et {}
# pour définir la valeur à imprimer et à utiliser quel format
print('a = {}, b = {}, c = {}'.format(a,b,c))
print('a = {0}, b = {1}, c = {2}'.format(a**2,b,c))
print('a = {:f}, b = {:20s}, c = {:15.3e}'.format(a,b,c))
```

## Chaînes


```python
a="C'est une chaîne"
```


```python
len(a)
```

Beaucoup de commandes peuvent fonctionner sur des chaînes. Les chaînes, comme TOUT en python, sont des objets. Les méthodes sont exécutées sur des objets par points:


```python
a.upper()
```


```python
a.title()
```


```python
a.split()
```


```python
a.split()[1]
```


```python
a = "C'est une chaîne. Avec différentes phrases."
```


```python
a.split('.')
```


```python
a.split('.')[1].strip() # Nous définissons ici le caractère utilisé pour se diviser. 
                        # Le défaut est l'espace (une combinaison d'espaces)
```


```python
a = 'tra'
b = 'la'
print (' '.join((a,b,b)))
print ('-'.join((a,b,b)))
print (''.join((a,b,b)))
print (' '.join((a,b,b)).split())
print (' & '.join((a,b,b)) + '\\\\')
```

## Conteneurs: Tuples, listes et dictionnaires

### Liste:
Une collection d'objets. Peut être de différents types. Elle a un ordre.


```python
L = ['red','green','blue'] # Les crochets sont utilisés pour définir des listes
```


```python
type(L) # Affiche le type de L
```


```python
L[1]
```


```python
L[0] # Les indices commencent à 0 !!!
```


```python
L[-1] # Dernier élément
```


```python
L[-3]
```


```python
L = L + ['black', 'white'] # Le symbole d'addition sert à agréger les valeurs d'une liste. Voir ci-dessous d'autre façon.
```


```python
print(L)
```


```python
L[1:3] # L [start: stop]: éléments d'index i, où start <= i <stop !! l'élément stop n'est pas inclus!
```


```python
L[2:] # Les limites peuvent être omises
```


```python
L[-2:]
```


```python
L[::2] # L [start: stop: step] tous les 2 éléments
```


```python
L[::-1]
```

Les listes sont mutables: leur contenu peut être modifié.


```python
L[2] = 'yellow'
L
```


```python
L.append('pink') # Ajouter une valeur à la fin
L
```


```python
L.insert(2, 'blue')    #L.insert (index, objet) -- insérer l'objet avant indice
L
```


```python
L.extend(['magenta', 'purple'])
L
```


```python
L.append(['magenta', 'azul'])
L
```


```python
L.append(2)
L
```


```python
L = L[::-1] # ordre inverse
L
```


```python
L2 = L[:-3] # Coupant les 3 derniers éléments
print (L)
print (L2)
```


```python
L[25] # Out of range conduit à une erreur
```


```python
print(L)
print (L[20:25]) # Mais NON ERREUR lors du tranchage.
print(L[20:])
print (L[2:20])
```


```python
print (L.count('yellow'))
```

On peut µutiliser TAB pour rechercher les méthodes (fonctions qui s'appliquent à un objet)



```python
a = [1,2,3]
b = [10,20,30]
```


```python
print(a+b) # Peut-être pas ce que vous attendiez, mais plutôt logique
```


```python
print(a*b) # Ne multiplie pas l'élément par élément. Numpy fera ce travail.
```


```python
L = range(4) # Créez une liste. Notez que le paramètre est le nombre d'éléments, pas le dernier. Le point final est omise.
L
```


```python
L = range(2, 20, 2) # Tous les 2 entiers
L
```

### Tuples:
comme des listes, mais immuables


```python
T = (1,2,3)
T
```


```python
T2 = 1, 2, 3
print (T2)
type(T2)
```


```python
T[1]
```

Les tuples sont immuables


```python
T[1] = 3 # Ne marche pas!
```

### Dictionnaries
Un dictionnaire est essentiellement une table efficace qui mappe les clés des valeurs. C'est un conteneur non ordonné


```python
D = {'Christophe': 12, 'Antonio': 15} # Défini par {key : value}
```


```python
D['Christophe'] # Accéder à une valeur par la clé
```


```python
D.keys() # Liste des clés du dictionnaire
```


```python
D['Julio'] = 16 # Ajout d'une nouvelle entrée
```


```python
print(D)
```

## Structures de contrôle

### Exécution conditionnelle if - elif - else
L'exemple ci-dessous illustre la forme complète de cette structure. Les parties `elif...` et `else...` sont facultatives. Pour des tests multiples, on peut bien entendu cascader plusieurs parties `elif....`

Notez bien la présence du caractère : (double point) précédant le début de chaque bloc !



```python
a, b = 4, 5
if a > b:
    print("%f est supérieur à %f" % (a,b) )
elif a == b:
    print("%f est égal à %f" % (a,b) )
else:
    print("%f est inférieur à %f" % (a,b) )
```

### Boucle for
La boucle for permet d'itérer les valeurs d'une liste, d'un tuple, d'une chaîne ou de tout objet itérable. Comme dans les autres structures de contrôle, le caractère : (double point) définit le début du bloc d'instruction contrôlé par for.


```python
# Sur listes
lst = [10, 20, 30] 
for n in lst:
    print(n, end=' ')
```


```python
# Sur tuples
for index in range(len(lst)):
    print(index, lst[index])
```


```python
for index,val in enumerate(lst):
    print(index, val) # => même affichage que ci-dessus
```


```python
# Sur chaînes
voyelles = 'aeiouy'
for car in 'chaine de caracteres':
    if car not in voyelles:
        print(car, end='')

```

Pour itérer sur une suite de nombres entiers, on utilise souvent la fonction range (objet itérable) présentée plus haut.


```python
# Sur dictionnaires
carres = {}
for n in range(1,4):
    carres[n] = n**2
carres
```

###  Boucle while
La boucle while permet d'exécuter un bloc d'instruction aussi longtemps qu'une condition (expression logique) est vraie.

Notez aussi la présence du caractère : (double point) définissant le début du bloc d'instruction contrôlé par while.



```python
nb = 1 ; stop = 5
# Affiche le carré des nombres de nb à stop
while nb <= stop:
    print(nb, nb**2)
    nb += 1
```

## Fonctions, modules, packages, scripts

### Fonctions
De façon générale, on implémente une fonction lorsqu'un ensemble d'instructions est susceptible d'être utilisé plusieurs fois dans un programme. Cette décomposition en petites unités conduit à du code plus compact, plus lisible et plus efficace.

L'exemple ci-dessous illustre les principes de base de définition d'une fonction en Python :
- La première ligne `def nomFonction(arguments...):` définit le nom avec lequel on invoquera la fonction, suivi entre parenthèses de son(ses) éventuel(s) arguments (paramètres d'entrée) séparés par des virgules ; cette ligne doit se terminer par :
- Les instructions de la fonction (corps de la fonction) constituent ensuite un bloc qui doit donc être indenté à droite
- Au début du corps on peut définir, sous forme de chaîne/commentaire multi-ligne, le texte d'aide en-ligne (appelé docstrings) qui sera affiché avec `help(fonction)`
- Avec l'expression `return` on sort de la fonction en renvoyant optionnellement des données de retour sous forme d'un objet de n'importe quel type ; si l'on ne passe pas d'argument à return, la fonction retournera alors None (objet nul) ; dans l'exemple ci-contre, on retourne 2 valeurs que l'on a choisi d'emballer sous forme de tuple



```python
def somProd(n1, n2):
    """Fonction calculant somme et produit de n1 et n2
    Résultat retourné dans un tuple (somme, produit)"""
    return (n1+n2, n1*n2)
```


```python
help(somProd)
```


```python
somProd(3,10)
```


```python
somProd()  # erreur "somProd() takes exactly 2 args"
           # et même erreur si on passe 1 ou >2 args.
```

Une fonction étant un objet, on peut l'assigner à une variable, puis utiliser celle-ci comme un "alias" de la fonction !


```python
sp = somProd
sp(3,10)
```

Lors de l'appel à la fonction, il est aussi possible de passer les paramètres de façon nommée avec `paramètre=valeur`. Dans ce cas, l'ordre dans lequel on passe ces paramètres n'est pas significatif !

On peut en outre définir, dans la déclaration def, des paramètres optionnels. Si l'argument n'est pas fourni lors de l'appel de la fonction, c'est la valeur par défaut indiquées dans la définition qui sera utilisée par la fonction.



```python
def fct(p1, p2=9, p3='abc'):
    # 1 param. obligatoire, et 2 param. optionnels
    return (p1, p2, p3)
```


```python
print(fct())         # => erreur (1 param. oblig.)
```


```python
print(fct(1))  
```


```python
print(fct(1, 2))
```


```python
print(fct(1, 2, 3))
```


```python
print(fct(p3=3, p1='xyz'))
```

###  Modules
Un module Python (parfois appelé bibliothèque ou librairie) est un fichier rassemblant des fonctions et classes relatives à un certain domaine. On implémente un module lorsque ces objets sont susceptibles d'être utilisés par plusieurs programmes.

Pour avoir accès aux fonctions d'un module existant, il faut charger le module avec la commande `import`, ce qui peut se faire de différentes manières, notamment :

   a) `from module import *` : on obtient l'accès direct à l'ensemble des fonctions du module indiqué sans devoir les préfixer par 


```python
from math import *
```


```python
dir()    # => objets dans namespace, notamment ces fcts
```


```python
sin(pi/2)
```


```python
cos(pi)
```

   b) `from module import fct1, fct2...` : on ne souhaite l'accès qu'aux fonctions fct1, fct2... spécifiées


```python
from math import pi, sin
```


```python
dir()    # => objets dans namespace, notamment ces fcts
```


```python
sin(pi/2)
```


```python
cos(pi) 
```

   c) `import module1, module2...` : toutes les fonctions de(s) module(s) spécifié(s) seront accessibles, mais seulement en les préfixant du nom du module


```python
import math
```


```python
# math.<tab> => liste les fonctions du module
dir(math)         # => objets dans namespace
```


```python
help(math)        # => affiche l'aide sur ces fonctions
```


```python
help(math.sin)    # => aide sur la fct spécifiée (sin)
```


```python
math.sin(math.pi/2)
```


```python
cos(pi)           # => erreur (non préfixés par module)
```


```python
math.cos(math.pi)
```

d) `import module as nomLocal` : toutes les fonctions du module sont accessible en les préfixant du nomLocal que l'on s'est défini


```python
import math as mt
```


```python
# mt.<tab>  => liste les fonctions du module
```


```python
dir(mt)           # => objets dans namespace
```


```python
help(mt)          # => affiche l'aide sur ces fonctions
```


```python
mt.sin(mt.pi/2)
```


```python
math.sin(math.pi/2) # => erreur "name math not defined"
```


```python
mt.cos(mt.pi)
```
