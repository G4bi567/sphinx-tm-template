# Guide utilisateur


## Installation et mise en route

Afin de pouvoir lancer le projet sur un ordinateur, il faut respecter une série d’étapes. Si {index}`Visual Studio Code` est déjà installé, le numéro 1 n’a pas besoin d’être fait. Si Node.js l’est aussi, le numéro 2 n’a non plus besoin d’être fait.

1.	Télécharger et installer {index}`Visual Studio Code`. Le fichier .exe peut être retrouvé sur le site officiel : https://code.visualstudio.com/ ; il faut choisir la version adaptée au système d’exploitation de l'ordinateur, comme Windows, MacOs, Linux.

Visual Studio {cite:p}`VSC` Code, souvent abrégé en VSCode, est un logiciel libre de Microsoft pour Windows, Linux et MacOS. Il est conçu pour aider les développeurs à créer, déboguer et déployer des applications logicielles. VSCode offre des fonctionnalités telles que la complétion de code, la prise en charge du débogage, la prise en charge des extensions, etc. Il prend également en charge de nombreux langages de programmation, notamment C++, Python, {index}`HTML`, {index}`CSS`, {index}`Javascript`, TypeScript, etc. Un des points les plus avantageux est le grand nombre d’extensions, qui permet aux développeurs de personnaliser leur environnement de travail et d’améliorer leurs productivité.

2.	Télécharger et installer Node.js, grâce au lien suivant : https://nodejs.org/en/download.
Pour l’installation, il faut accepter des modifications en tant qu’administrateur.

Node.js {cite:p}`Node,Node2` est un environnement d’exécution {index}`Javascript` côté serveur. Grâce à ce framework, les développeurs disposent d’un interpréter du code {index}`Javascript` en dehors du navigateur. La distribution de Node.js intègre NPM, ou Node Package Manager. NPM {cite:p}`Node,Node2` est un environnement d’exécution {index}`Javascript` côté serveur. Grâce à ce framework, les développeurs disposent d’un interpréter du code {index}`Javascript`. La distribution de Node.js intègre NPM, ou Node Package Manager. NPM est un gestionnaire de paquets pour Node.js qui permet aux développeurs de gérer facilement les dépendances de leur projet. NPM facilite l’installation, la mise à jour et la suppression des paquets et des modules nécessaires à un projet. Cela permet aux développeurs de créer des applications de bureau multiplateformes à l’aide de technologies Web telles que {index}`HTML`, {index}`CSS` et {index}`Javascript`.

3.	Faire une vérification pour savoir si Node.js et NPM sont correctement installés. Il faut ouvrir le terminal sur {index}`Visual Studio Code` en allant sur Affichage > Terminal ou Terminal > Nouveau Terminal. Puis il faut écrire les deux commandes suivantes séparément et ensuite, il faut appuyer sur enter. 

	```bash

	node -v

	```
	```bash

	npm -v

	```
	Ces deux commandes permettent de donner la version de Node.js et NPM.

4.	Installer yarn avec le terminal en écrivant le code suivant et en appuyant sur enter :
	```bash

	npm install --global yarn
	```

Yarn NPM {cite:p}`yarn` est un gestionnaire de paquets pour {index}`Javascript`, créé par Facebook, et est compatible avec NPM et Node.js. Un des avantages par rapport à NPM est le fait qu’il arrive à installer les dépendances et les paquets plus rapidement. 

5. Télécharger et extraire le code du projet sur https://github.com/G4bi567/quasar-projet-true-form. Il faut ensuite ouvrir le dossier en le glissant dans {index}`Visual Studio Code` ou en allant dans Fichier > Ouvrir le dossier > ... et en choisissant le dossier du travail. Ce projet est stocké sur {index}`GitHub`, si Git est installé sur la machine utilisée, il est aussi possible d'utiliser la commande suivante dans le terminal afin d'installer le projet :

	```bash

	git clone https://github.com/G4bi567/quasar-projet-true-form

	```

6.	Installer les indépendances avec le terminal en écrivant :
	```bash

	yarn install
	```


7.	Pour accéder au projet, il faut exécuter dans le terminal :
	
	```bash

	quasar dev
	```

Cela démarre le serveur de développement et un nouvel onglet s’ouvre. Si rien ne s’ouvre, il faut positionner la souris sur http://localhost..., appuyer sur la touche « ctrl » et faire un click gauche.


## Présentation des principales fonctionnalités 

### Connexion et déconnexion

Lors de l’arrivée sur le site, un nom, un mail et un mot de passe sont demandés. Cette fonctionnalité est intégrée afin de donner une meilleure immersion dans le forum. Ces données ne sont pas toutes utilisées dans la version fournie, car aucun backend a été mis en place. Seulement le nom est utilisé en vue de compléter les publications écrites par l’utilisateur. Puis, une fois connecté, il est tout à fait possible de se déconnecter. Cette option se trouve dans le menu paramètre.

### Créer des publications et des commentaires

La fonctionnalité la plus importante de ce site est la possibilité de créer ou de répondre à une publication. Tout d’abord, en vue de créer une publication, il est très facile de repérer le bouton « une question ». L’utilisateur peut alors compléter les paramètres de sa publication et l’envoyer dans la base de données. Tout de suite, il est possible de voir que la nouvelle publication a été ajoutée. Puis, le commentaire de publication fonctionne de la même façon. Cependant, cette fois-ci, seule la réponse est importante, car les autres paramètres sont déjà complétés. 

### Suppression

L’option « Supprimer » est très importante. Il est possible de supprimer les publications écrites par l'utilisateur. Cette fonctionnalité supprime la publication complète ; il n'est pas possible de supprimer les commentaires des publications.

### Filtrage des publications

Afin d’améliorer l’usage du forum, des fonctions filtrent les publications. Par exemple, en appuyant sur le nom d’une personne dans une publication, il est possible de voir toutes les publications de cet utilisateur. La même fonctionnalité s’applique à la branche associée à la publication, dans le but de voir toutes les publications liées à cette branche précise. À gauche, une liste des branches déroulante est présente, et facilite l’accès rapide à toutes les branches. Une autre fonction de filtrage est présente pour le nombre de publications affichées sur une page. Le site affiche jusqu'à 5 publications par page. Lorsque le site contient plus de 5 publications, il est possible de changer de page avec le menu de navigation afin de voir les autres publications

### Suivis

La page Suivis permet de voir les publications que l’utilisateur a aimées grâce au bouton cœur présent sur les publications. Ceci permet de suivre une publication, si la réponse à la problématique intéresse l'utilisateur.

### Liens utiles 

Dans le but d’aider les étudiants, le site donne accès à des outils intéressants. Ils sont accessibles sous forme de liens URL dans le tiroir à droite. Voici un exemple :

```{figure} figures/exemple_tiroir_liens.png
---
width: 30%
---
Tiroir des liens utiles
```

Les tiroirs sont des listes qui peuvent être cachées. Ils permettent une manière de fournir des informations dans un site Web qui est dynamique est simple à comprendre.
    

### Changement de photo de profil

Il est tout à fait possible de changer de photo de profil. Dans le but d'accéder à cette fonctionnalité, l'utilisateur doit se rendre dans les paramètres du site. Il pourra alors y coller un lien d'une photo. Si le lien utilisé n'est pas une image,  la fonction ne s’exécutera pas.


	
