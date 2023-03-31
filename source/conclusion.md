
# Conclusion 



## Bilan des objectifs

Le projet est une réussite. 
Pour commencer, le design du site est ressemblant à celui établi dans la maquette. 
Ensuite, les fonctionnalités basiques ont été implémentées, comme la création de publications et la possibilité de créer des commentaires. 
Il a été difficile de lier les deux fonctionnalités comme elles le sont maintenant. 
Même ayant des points communs, la fonction travaille avec deux types de variables afin de s'adapter aux deux types de requête. 

Des tiroirs ont aussi été ajoutés; ils permettent une meilleure compréhension et une meilleure utilisation du site. 
Puis de nouvelles fonctionnalités ont été ajoutées. 
Les fonctions de filtrage permettent à l'utilisateur de se trouver sur des pages filtrées par le paramètre choisi. 
La page "suivis" a été implémentée, ce qui facilite l'utilisation du site. 
La connexion et la déconnexion sont des tâches accomplies même si elles sont fictives. 
Cette création de profil est primordiale, en vue de créer des publications avec les noms des auteurs. 
De plus, les paginations ont été oubliées lors de la définition des objectifs. 
Il ne s'agit pas d'une fonctionnalité très attrayante, mais elle est extrêmement utile afin de garder une unicité et une élégance dans le projet. 

Cependant, certaines fonctionnalités prévues au début du travail n’ont pas été implémentées, car lors de la modélisation et de la définition des objectifs du travail, le projet a été surestimé ??? n'est-ce pas plutôt sous-estimé ???
Le projet est le premier travail fait après l'apprentissage de la programmation web, ce qui explique le manque d’expérience dans la mise en place de ce projet. 
Par exemple, il était prévu d'intégrer le backend dans le projet. 
Les séminaires n’ont malheureusement pas donné la possibilité d’apprendre à en utiliser un. 
D'autres fonctionnalités plus basiques ont été volontairement mises de côté. 
Par exemple, le changement de couleur du site qui a été considéré comme une fonctionnalité secondaire et n'a finalement pas été implémenté.

### Propositions de piste pour accomplir les objectifs  

Avec plus de temps, il est tout à fait envisageable d'implémenter ces fonctionnalités. 
Afin de créer un site avec la possibilité de changer de couleur, il est possible d'utiliser les variables SCSS, déjà fournies par l’application Quasar, et de les changer grâce à des palettes de couleur, placées dans les paramètres du site. 
De plus, une nouvelle variable dans le store « comment.js » peut être créée, dans le but d’enregistrer les points forts de l’élève. 
Ensuite, une nouvelle page ou un bouton qui sert de filtre peuvent être utilisés afin d’afficher les publications qui sont adaptées aux choix faits préalablement.

## Présentation des défauts du code  

Le projet contient quelques défauts. Pour commencer, n'importe quel utilisateur peut supprimer une publication qu'il n'a pas écrit. Ce type de fonctionnalité est souvent disponible pour les administrateurs d'un site. Dans le futur, le projet pourrait ,grâce à une vrai connexion, restreindre l'utilisateur de pouvoir supprimer uniquement ses propres publications. L'autre défaut est le manque de confirmatio

## Travaux futurs pour le site

L'un des problèmes lors de la finalisation d'un travail créatif est le fait qu'il y a toujours de nouvelles fonctionnalités et de nouveaux outils à implémenter. 

Pendant la présentation du projet, le composant récursif « LayerPostComment » a été présenté. 
Cependant, pour la création de publications et de commentaires, ce schéma devient plus compliqué à mettre en place. 
Il faut avoir un gestionnaire de données capable de trouver l’emplacement où il faudrait ajouter le commentaire, car, avec la méthode actuelle, il est difficile d’ajouter un commentaire à un commentaire précédent d’une manière effective. 
La même logique s’applique lorsque l’utilisateur veut supprimer un commentaire, il est impossible de retrouver l’index d’un commentaire facilement. 
Ce problème peut être résolu grâce à l'implémentation d'un backend, qui permet de gérer les données avec plus d'aisance.

Pendant la présentation du projet, le composant récursif « PostLayer » a été présenté. 
Cependant, pour la création de publications et de commentaires, ce schéma devient plus compliqué à mettre en place. 
Il faut avoir un gestionnaire de données capable de trouver l’emplacement où il faudrait ajouter le commentaire, car, avec le projet actuel, il est impossible d’ajouter un commentaire à un commentaire d’une manière effective. 
La même logique s’applique lorsque l’utilisateur veut supprimer un commentaire, il est impossible de retrouver l’index d’un commentaire facilement.
Dans le but de faire un site qui plait à tous les utilisateurs, c’est une bonne idée d’ajouter dans les paramètres du site internet une palette de couleur qui peut changer les couleurs du site internet. Le problème est que pour l’implémentation de cette fonctionnalité, il faut des connaissances plus avancées dans le scss et les différents plugins.




