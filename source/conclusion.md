

# Conclusion 

## Présentation des bogues connus restant dans la version finale  

À trouver

## Bilan des objectifs

Des fonctionnalités prévues au début du travail n’ont pas été implémentées, car lors la modélisation et les objectifs du travail, le projet a été surestimé. Le projet est le premier travail fait après l'apprentissage de la programmation web, ce qui montre le manque d’expérience dans la mise en place de ce projet. Par exemple, le backend était prévu d’être intégré dans le projet. Les séminaires n’ont malheureusement pas donné la possibilité d’apprendre à en utiliser un. Cependant, des fonctionnalités plus basiques ont été mises de côté. Comme le changement de couleur du site, il a été considéré comme une fonctionnalité secondaire, et n'a finalement pas été implémenté. En plus, la possibilité à l’utilisateur de fournir les branches dans lesquelles il est à l’aise n’a aussi pas été faite.

### Propositions de piste pour accomplir les objectifs  

Avec plus de temps, il est tout à fait envisageable de pouvoir implémenter ces fonctionnalités. Afin de créer un site avec la possibilité de changer de couleur, il est possible d'utiliser les variables SCSS, déjà fournies par l’application quasar, et de les changer grâce à des palettes de couleur, placées dans les paramètres du site. De plus, une nouvelle variable dans le store « comment.js » peut être créée, dans le but d’enregistrer les points forts de l’élève. Ensuite, une nouvelle page ou un bouton qui sert de filtreur peuvent être utilisés afin d’afficher les publications qui sont adaptées aux choix fait au préalable.

## Proposez des fonctionnalités supplémentaires qu'il serait bon de développer 

L'un des problèmes lors de la finalisation d'un travail créatif est le fait qu'il y a toujours de nouvelles fonctionnalités et de nouveaux outils à implémenter. 

Pendant la présentation du projet, le composant récursif « LayerPostComment » a été présenté. Cependant, pour la création de publications et de commentaires, ce schéma devient plus compliqué à mettre en place. Il faut avoir un gestionnaire de données capable de trouver l’emplacement où il faudrait ajouter le commentaire, car, avec la méthode actuelle, il est impossible d’ajouter un commentaire à un commentaire d’une manière effective. La même logique s’applique lorsque l’utilisateur veut supprimer un commentaire, il est impossible de retrouver l’index d’un commentaire facilement. Ce problème peut être résolu grâce à l'implémentation d'un backend, qui permet de gérer les données avec plus d'aisance.


## Travaux futurs pour le site

Mise en ligne sur un serveur 
Développement d’un backend
Création d’un vrai login 


