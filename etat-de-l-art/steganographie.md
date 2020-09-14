# Définitions
* La stéganographie est assimilée à l'art de dissimuler des données dans d'autres données.
* Stéganographie viens du Grec. En effet, il est composé du mot 'steganos' qui veut dire caché et du mot 'graphein' qui veut dire écriture.

# Principes de la stéganographie
## Applications
Voici les différents applications dans le domaine de la stéganographie :
- Communiquer secrètement
- Exfiltrer de l'information
- Marquer une information de manière à  pouvoir l’authentifier, la tracer ou attribuersa propriété intellectuelle = watermarking

## Propriétés d'une technique de stéganographie
### La capacité
Cette propriété représente la quantité d’information qui peut être dissimulée. Le fichier porteur dispose d’une quantité limitée d’espace pour stocker ses propres informations.

### Résistance à la détection
Plus une technique a la propriété d’être transparente, plus il est difficile de détecter que le fichier contient une information.

### Résistance à la destruction
Une technique robuste permet de résister aux traitements du signal qui pourraient altérer le fichier porteur et détruire le message.

# Un peu d'histoire
## Les esclaves
Le premier historien à en parler Hérodote (484 à 445 av J.-C.). Un prisonnier retenu à Suse par le roi des perses désirait transmettre un message à son roi.
Il rasa les cheveux d'un esclave, écrit son message sur le crâne de celui-ci et se mit à attendre que ses cheveux repoussent.
Il l'envoya alors à son roi sachant qu'il serait fouillé mais que son message passerait inaperçu.

## Tablette de cire
Démarate, roi de Sparte, écrivait ses messages sur tablette de bois qu'il recouvrait de cire.
Ses interlocuteurs n'avaient plus qu'à gratter la cire et lire leurs messages.

## Jus de citron
En écrivant avec du citron, le message est invisible. Mais, en passant la feuille devant une flamme, le message apparait.

# Les algorithmes informatiques
## Least significant Bit
Cette technique permet de cacher un message dans une image. pour cette technique, chaque bit de poids faible d'un pixel va être modifié pour y intégrer de l'information.

## F5
Cet algorithme permet de cacher des données dans des images JPEG. Cet algorithme cache l'information au moment de la compression. Elle est plus longue à implémenter que le LSB.

## NSF5
Il a été créé pour corriger les faiblesses de l’algorithme F5. 

## MOD
L’algorithme MOD proposé par étend la proposition d'algorothme HUGO en définissant un coût de détectabilitéρi paramétré par un nombre élevé de paramètres.

## Echo Hiding
La technique de l’Echo Hiding consiste à encoder l’information en introduisant un courtécho dans le signal audio. En dessous d’un délai d’une milliseconde,l’écho n’est pas perceptible par l’oreille humaine. L’inconvénient de cette méthode est sa faible capacité due à lamilliseconde d’écart nécessaire pour conserver sa transparence, ce qui explique le nombre limité de travaux surles applications de cette technique.

## HUGO
Est une méthode de stéganographie d'image bien connue proposée ces dernières années. Il a joué un rôle prépondérant dans les algorithmes de dissimulation adaptatifs actuels. 

## Ajustement DC
Cet algorithme traite seulement les images de format JPEG où l'image RGB est convertie en YCbCr. La dissimulation des données n’est réalisée que dans le plan Y qui contient l’essentiel de l’information.  Cet  algorithme  possède  comme  entrée  le  message secret et l'image porteuse, et comme sortie l'image dite stégo.

## DWT-LSB 
Cet  algorithme  introduit   par possède  de  manière  naturelle  en  entrée l'image porteuse et l'image secrète, et en sortie l'image stégo. Il cache un seul bit du message secret dans le LSB d'un coefficient DWT en se basant sur un certain seuil. 

## DWT Alpha- Fusion 
Cet  algorithme  fut  introduit  dans  [Boora  et  Gambhir,  2013].  Le  principe  est  de  crypter l'image secrète via la carte d’Arnold, puis d’effectuer une transformée DWT à la fois sur l'image cryptée et sur l'image porteuse. Les deux transformées sont ensuite fusionnées (selon le modèle donné par l’eq. 3.1) . En final, on applique une transformée inverse (IDWT) pour obtenir  l'image  stégo.  Dans  cet  algorithme,  Les  deux  images,  secrète  et  porteuse  sont  de même  taille.  Le  cryptage  et  le  fusionnement  donnent  à  ce  type  de  stéganographie  un  bon niveau de sécurité. 

# Les logiciels de stéganographie
## Steghide
Steghide est un logiciel disponible sur les distributions Linux. Il permet de dissimuler du texte dans différents types de fichiers (BMP, JPG, WAV, AU, ...)

## Mp3Stego
Outil permettant de cacher de la donnée dans un mp3 ou wav.

## Stegsolve
Permet de manipuler des images en fonction des pixels, filtres, ...

## Stegoveritas
Outil disposant de nombreuses fonctionnalités :  vérifier les métadonnées, créer de nombreuses images transformées, Brute forces LSB, ..

## Zsteg
Permet de détecter le type de stéganographie du fichier (LSB openstego, Camouflage ...)

## Stegdetect
Effectue des tests statistiques pour déterminer si un outil stego a été utilisé jsteg, outguess, jphide, ...

## tegbreak
Brute forcer pour JPG (Pour les méthodes outguess, jphide et jsteg)

## Jphide
Permet de dissimuler/extraire de la donnée cachée dans un JPG
