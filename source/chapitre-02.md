# Guide utilisateur
## Installation et mise en route

Afin de pouvoir lancer le projet sur un ordinateur, il faut respecter une série d’étapes à suivre. Si Visual Studio Code est déjà installé, le numéro 1 n’a pas besoin d’être fait. Si Node.Js l’est aussi, le numéro 2 n’a non plus besoin d’être fait.

1.	Télécharger et installer Visual Studio code, le fichier .exe peut être retrouvé sur le site officiel : https://code.visualstudio.com/ , il faut choisir la version adaptée au système d’exploitation personnelle, comme par exemple Windows, MacOs, Linux.

Visual Studio Code est un logiciel libre de Microsoft pour Windows, Linux et macOS. Il est conçu pour aider les développeurs à créer, déboguer et déployer des applications logicielles. Il peut s’abréger en VS Code. Celui-ci offre des fonctionnalités telles que l’achèvement du code, la prise en charge du débogage, la refactorisation du code, l’intégration git, la prise en charge des extensions, etc. Il prend également en charge de nombreux langages de programmation, notamment C++, Python, HTML, CSS, JavaScript, TypeScript, etc. Puis, un des points les plus avantageux est le grand nombre d’extensions. Ceci permet aux développeurs de personnaliser leur environnement de travail et d’améliorer leurs productivités.

2.	Télécharger et installer Node.Js, grâce au lien suivant : https://nodejs.org/en/download.
Pendant l’installation, il faut accepter des modifications en tant qu’administrateur.

Tout d’abord, Node.js est un environnement d’exécution JavaScript côté serveur. Sans ce framework, il serait impossible pour les développeurs d’interpréter du code Java en dehors du navigateur. Ensuite avec la distribution de Node.js vient intégrer NPM. NPM, ou Node Package Manager, est un gestionnaire de paquets pour Node.js qui permet aux développeurs de gérer facilement les dépendances de leur projet. NPM facilite l’installation, la mise à jour et la suppression des paquets et des modules nécessaires à un projet. Cela permet aux développeurs de créer des applications de bureau multiplateformes à l’aide de technologies Web telles que HTML, CSS et JavaScript.

3.	Faire une vérification pour savoir si Node.js et NPM sont correctement installés. Il faut ouvrir le terminal sur Visual Studio Code en allant sur Affichage > Terminal ou Terminal > Nouveau Terminal. Puis il faut écrire les deux commandes suivantes séparement et ensuite, il faut appuyer sur enter. 
	```bash

	node -v

	```
	```bash

	npm -v

	```


4.	Installer yarn avec le terminal en écrivant « npm install --global yarn » et en appuyant sur enter.

Yarn est un gestionnaire de paquets pour JavaScript. Il a été créé par Facebook. Il est compatible avec npm et Node.js. Un des avantages par rapport à npm est le fait qu’il arrive à installer les dépendances et les paquets plus rapidement. Il a été mis en place dans le but de répondre à certaines limitations et des problèmes de performances de npm.


5.	Installer les indépendances avec le terminal en écrivant « yarn install ».


6.	Installer Quasar en exécutant la commande suivante dans le terminal. « npm install -g @quasar/cli »


7.	Pour accéder au projet, il faut exécuter « quasar dev » dans le terminal. Cela démarrera le serveur de développement. Finalement, un nouvel onglet s’ouvre. Cependant si rien ne s’ouvre, il faut appuyer sur « ctrl +click » dans le terminal sur http://localhost... .

## Présentation des principales fonctionnalités 
### Connection et déconnection
Lors de l’arrivée sur le site, il est directement demandé un nom, un mail et un mot de passe. Cette fonctionnalité est intégrée afin de donner une meilleure immersion dans le forum. Ces données ne sont pas toutes utilisées dans la version fournit, car aucun backend a été mis en place. Seulement le nom est utilisé en vue de compléter les publications écrites par l’utilisateur. Cela permet de fournir des indications sur qui a écrit quelque chose. Puis, une fois connecté, il est tout à fait possible de se déconnecter dans le but de créer des nouvelles publications avec des écrivains différents. Cette option se trouve dans le menu profil.
### Créer des publications et des commentaires
La fonctionnalité la plus importante de ce site est la possibilité de créer une publication ou d’en répondre à une. Tout d’abord, en vue de créer une publication, il est très facile de repérer le bouton « une question ». L’utilisateur peut alors compléter les paramètres de sa publication et l’envoyer dans la base de données. Tout de suite, il est possible de voir que la nouvelle publication a été ajoutée. Puis, le commentaire de publication fonctionne de la même façon. Cependant, cette fois-ci, seule la réponse est importante, car les autres paramètres sont déjà complétés. Le problème avec la création d’un commentaire, c’est qu’il est très compliqué de trouver l’endroit où ajouter le commentaire sans un outil de recherche avancé.
### Suppression
L’option de supprimer est très importante. Afin dans le futur, lors d’une vraie utilisation de la connexion avec un compte, il est possible de supprimer les publications personnelles et non toutes. il est possible de supprimer toutes les publications, même si l’ utilisateur ne les a pas écrites. Cette option n’est utilisée que pour les publications et non les commentaires. 
### Filtrage des publications
Afin d’améliorer l’usage du forum, des actions filtrent les publications. Par exemple, en appuyant sur le nom d’une personne dans une publication, il est possible de voir toutes les publications de cet utilisateur. La même fonctionnalité s’applique à la branche de la publication, dans le but de voir toutes les publications liées à cette branche précise. Pour plus de filtrage, une liste des branches déroulante à gauche est présente, en vue de faciliter l’accès à toutes les branches très rapidement. Une autre fonction de filtrage est aussi présente pour le nombre de publication affichée une page. Ce nombre est fixé à 5. Si ce nombre est dépassé, alors il apparaît au bas de la page, dans la pagination, le nombre de pages nécessaires afin de pouvoir afficher toutes les publications.
###Suivis
La page Suivis permet de voir les publications que l’utilisateur a aimé grâce au bouton cœur présent sur les publications. Ceci permet de suivre une publication, si la réponse à la problématique intéresse l'utilisateur.
### Liens utiles 
Dans le but d’aider les étudiants, le site donne accès à des outils intéressants. Ils sont accessible sous forme de liens url dans le tiroir à droite. Voici un exemple :
 
Les tiroirs sont des listes qui peuvent être cachées. Ils permettent une manière de fournir des informations dans un site Web qui est dynamique est simple à comprendre.
	


	
