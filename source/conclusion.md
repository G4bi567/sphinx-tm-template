
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

Cependant, certaines fonctionnalités prévues initialement, telles que les questions adaptées à chaque utilisateur, n'ont pas été implémentées. Cela est dû à une sous-estimation du travail lors de la modélisation et de la définition des objectifs du projet.
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

## Travaux futurs pour le site

L'un des problèmes lors de la finalisation d'un travail créatif est le fait qu'il y a toujours de nouvelles fonctionnalités et de nouveaux outils à implémenter. 

Pendant la présentation du projet, le composant récursif « LayerPostComment » a été présenté. Cependant, la mise en place de commentaires imbriqués devient plus complexe avec cette approche. Il est nécessaire d'avoir un gestionnaire de données capable de déterminer l'emplacement où ajouter le commentaire, car la méthode actuelle ne permet pas d'ajouter efficacement un commentaire en réponse à un commentaire précédent. De même, il est difficile de retrouver l'index d'un commentaire pour le supprimer.
Ces problèmes pourraient être résolus en mettant en place un backend qui facilite la gestion des données. Avec l'implémentation d'un backend, il serait possible de créer un formulaire de connexion plus fonctionnel. De plus, il serait envisageable de mettre en place un rôle administrateur qui aurait la capacité de gérer tous les commentaires et de les supprimer.
L'intégration d'un backend offre des possibilités plus avancées de gestion des données et permettrait d'améliorer ces fonctionnalités dans le projet.