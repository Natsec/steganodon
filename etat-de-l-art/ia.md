# Machine Learning

* sous-discipline de l'IA ; 
* apprentissage automatique ;
* repose sur un **modèle** : représensation d'un modèle donné ;

Un **modèle** est une représentation mathématique qui permet de modéliser des règles par rapport aux données. 

La modélisation des données se compose de deux phases : l'**apprentissage** et la **prédiction**. 

Il existe trois façons d'apprendre pour un programme d'IA : l'apprentissage supervisé, non supervisé et essai/erreur. 

**Obj** : créer un programme capable de collecter toutes les données disponibles pour un problème donné, et d'apprendre lui-même à partir de ces données pour construire son propre modèle.

## Méthode 1 : l’apprentissage supervisé

* **caractéristiques** : détails de l'objet à analyser ;
* **étiquettes** : cible à prédire ; connue lors de l'entraînement MAIS à déterminer en production ;

## Méthode 2 : l’apprentissage non supervisé 

* pas d'étiquette : l'algorithme ne sait pas à l'avance ce qu'il va trouver ;
* faire créer des groupes puis les nommer ;

## Méthode 3 : l’apprentissage par essai/erreur

* agent (algo) en interaction avec un environnement (caractéristiques) ; 
* trouver par tâtonnements successifs ; 
* trouver une solution optimale ; 
* algo auto-adaptatif : apprentissage constant ;

## Phase de prédiction 

Pendant la phase d'apprentissage, le programme utilise des données existantes, déjà connues. Une fois qu'il a appris et qu'il est bien entraîné (en utilisant l'une des trois méthodes), il peut dès lors être utilisé pour de la prédiction. 

1. Méthode supervisée : en rentrant de nouvelles caractéristiques, l’algorithme va pouvoir nous estimer le prix d’un bien. 

2. Méthode non supervisée : on peut identifier une nouvelle zone géographique, on regarde à quelle zone connue elle ressemble et on lui applique les mêmes règles. 

3. En essai/erreur : l'algorithme ne prédit pas, il réessaye. 

# Deep Learning

* sous-discipline du Machine Learning ;
* apprentissage profond ; 

Construction de systèmes inspirés de nos cerveaux, comportant des **réseaux de neurones artificiels**.

Principe de **convolution**, qui permet d'analyser une image pas à pas avec une fenêtre de filtre et donc d'être plus performant.

## Réseaux de neurones artificiels

Rpz par une boîte noire : 

1. une entrée : data fournie ;
2. un réseau neuronal : couches successives de neurones artificiels ; on parle de couches intermédiaires en interactions avec des opérations mathématiques ; neurons activés ou non (fonction d'activation) ;
3. une sortie : résultat attendu ;

## Convolution

Réponse au problème de sensiblité extrême des réseaux : un petit changement de la donnée entraîne un boulversement interne et donc des perfs médiocres.

La convolution n’est rien d’autre qu’un filtrage d'une image. Plutôt que de traiter l'image en un bloc, nous allons la diviser en différents carrés que nous allons analyser séparément.
