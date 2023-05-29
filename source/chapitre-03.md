# Guide développeur

## Structure du code et rôles des fichiers

Cette section présente une analyse approfondie de tous les fichiers du projet.

- src/boot/.gitkeep
    * Ce fichier {cite:p}`gitignore_gitkeep` n’est pas un fichier spécifique à {index}`Quasar`, mais un fichier ajouté par Git. Il permet d’inclure des répertoires vides dans le dépôt du projet.
- src/components/CreatePostComment.vue
    * Le composant permet à l’utilisateur de poser une question, c’est-à-dire de créer sa publication. Ce composant permet de recueillir des données. 
    ```{figure} figures/CreatePost_composant.png
    ---
    width: 50%
    ---
    Exemple du composant « CreatePostComment ». 
    ```
    * Tout d’abord, l’utilisateur doit fournir la branche sur laquelle il a un questionnement. Puis, il doit écrire un titre pour sa publication. Finalement, il doit rédiger une description détaillée, en vue de faire comprendre le mieux possible le problème aux autres utilisateurs. La description peut être mise en forme grâce aux options de police et de format.  Le composant se termine par un bouton de soumission « Envoyer » qui permet d’activer la fonction qui enregistre la publication. Puis l’utilisateur est envoyé sur la page d’accueil avec la nouvelle publication présente. La fonction « addPost », qui permet d’enregistrer la nouvelle publication, sera expliquée plus en détail dans src/stores/comment.js.
    * Une fonctionnalité intéressante sur ce composant est la fonction « isAvailable ». 
    
    ```{literalinclude} project/src/components/CreatePostComment.vue
    :language: html
    :caption: src/components/CreatePostComment.vue
    :linenos: true
    :lines: 142-162
    ```
    * Lors de la création de la publication, il faut absolument que les 3 entrées soient remplies. Cette fonction permet de bloquer les actions lorsque le bouton de soumission est activé. Elle active la variable du {index}`store` "isAvailableVar", en affectant la valeur "false". Cette variable commence par empêcher le changement de page, lors de l’appel de la fonction « $emit('finished') » et affiche une phrase « il manque au moins une entrée ». Si toutes les conditions sont respectées, toutes les actions sont effectuées.
- src/components/LayerPostComment.vue
    * Le composant actuel permet de créer un modèle pour les publications et pour les commentaires. 
     ```{figure} figures/comment.png
    ---
    width: 60%
    ---
    Exemple du composant « LayerPostComment ». 
    ```
    * Ce composant prend en paramètre les données fournies par le composant « CreatePostComment », vu précédemment. Premièrement, il affiche, sur la partie supérieure gauche, la photo de profil et le nom de l’utilisateur. Cette partie est cliquable et permet d’envoyer l’utilisateur sur la page du profil en question. Ensuite, sur la partie supérieure droite, un menu déroulant est présent. Lorsque ce menu est ouvert, une option « supprimer » apparaît. Celle-ci donne la possibilité de supprimer la publication. Puis, la partie du centre est composée du nom de la branche, du titre de la publication et la description du problème. Le nom de la branche est cliquable et dirige l’utilisateur sur une page dédiée aux publications de la branche choisie. Sur la partie inférieure se trouvent des fonctionnalités plus interactives. Tout d’abord, un bouton cœur permet d’enregistrer une publication dans les suivis. Le bouton en forme de bulle permet d’afficher la partie des commentaires ci-dessous.
    ```{figure} figures/comment_partie_commentaire.png
    ---
    width: 50%
    ---
    Exemple de la partie commentaire du composant « LayerPostComment ». 
    ```
    * Les personnes voulant répondre à la publication, peuvent créer un commentaire. Il suffit d’écrire la résolution du problème. Puis, grâce au bouton « Répondre », le commentaire est ajouté dans le site. 
    * La spécialité de ce composant est qu’il est récursif. Un composant récursif est un composant qui s’appelle lui-même. Cela permet de faire des publications avec des commentaires qui ont des commentaires, etc…  Voici un schéma pour mieux comprendre les fonctions récursives.  

    ```{figure} figures/Diagramme_recursive.png
    ---
    width: 60%
    ---
    Explication de la récursivité.
    ```
    * Grâce à la récursivité, il n’y a pas besoin d’avoir d’autres composants modèles. Les commentaires des publications n’ont pas de titres et de branches, mais grâce à des conditions, il est possible de garder toujours le même composant.
- src/scss/app.scss
    * Un fichier scss {cite:p}`scss` pour l’ensemble de l’application. C’est-à-dire des styles globaux qui pourront être utilisés dans tout le code. Il est automatiquement généré par {index}`Quasar` lors de la création d’un nouveau projet.
- src/scss/quasar.variables.scss
    * Ce fichier {cite:p}`scss` permet de créer des variables qui sont utilisées pour la personnalisation des composants. Il est aussi automatiquement généré par la création d’un nouveau projet {index}`Quasar`. 
- src/layouts/MainLayout.vue
    * Le MainLayout est la base du projet. Ce fichier définit la barre de navigation, affichée en haut du site. 
    ```{figure} figures/MainLayout.png
    ---
    width: 60%
    ---
    Exemple du « MainLayout ».
    ```

    
    * Cette barre permet d’accéder à plusieurs fonctionnalités du site. Tout d’abord, des boutons « Home page » et « Suivis » sont présents. Ils permettent d’accéder soit à la page principale des publications, soit à la page réservée aux publications suivies. Le bouton « Home Page » sert à remettre à zéro la page lorsqu’un filtre est utilisé. La page « Suivis » est utile à l’utilisateur, afin de voir l’évolution de la discussion pour résoudre un problème. Ensuite, une image du logo du Collège du Sud et le titre « Forum CSUD » font office de titre pour le site Web. Puis, un bouton « Une question » donne accès au formulaire de création de publication comme vu précédemment dans le composant « CreatePostComment ». Finalement, il y a un menu déroulant qui permet d’accéder à la page des paramètres du site.
    * Les deux boutons aux extrémités permettent d’ouvrir des « drawers », c’est-à-dire des tiroirs. Du côté gauche, les branches sont affichées. Lorsque l’utilisateur clique sur une des branches, il est amené sur la page relative et ne peut alors voir que les publications liées à cette branche. Du côté droit, des liens utiles pour les étudiants sont affichés et permettent un accès facile à des outils pertinents pour les élèves.
    * La suite du code permet d’afficher les composants et les pages principales du site. Cette fonctionnalité est établie grâce à des conditions sur la base de variables qui changent lorsque l’utilisateur accède aux pages du site. Voici le code:
    ```{literalinclude} project/src/layouts/MainLayout.vue
    :language: html
    :caption: src/layouts/MainLayout.vue
    :linenos: true
    :lines: 89-102
    ```
    * L’affichage de la page varie principalement entre trois pages.
    * Tout d’abord, la page de connexion. Cette page est la première page à s’afficher pour un nouvel utilisateur. Le site n’ayant aucune information sur le profil à ce moment-là, la variable « isLogVar » a la valeur « false » et permet ainsi à la page « LogInPage » d’apparaître. Une fois le formulaire de connexion rempli, la variable est égale à « true ». Alors s’affiche la deuxième page, c’est-à-dire le fil des récentes publications dans l’ordre de publication. Cette page est faite grâce à « IndexPage.vue ».  Puis, si l’utilisateur décide d’écrire une question, en appuyant sur le bouton «une question», la variable « writeComment » est égale à « true ». Ainsi, le composant « CreatePostComment » apparaît. Une fois le formulaire rempli, la valeur « false » est affectée à la variable et la page de fil des publications s’affiche en conséquence.

- src/pages/ErrorNotFound.vue
    * La page « ErrorNotFound.vue » est une page qui s’affiche lorsque l’utilisateur essaye d’ouvrir une page inexistante. Dans cette situation, une erreur 404 est affichée, indiquant que la route URL n’a pas été définie. 
    * Le design peut être vu dans la Fig. 6.
    ```{figure} figures/error_page.png
    ---
    width: 40%
    ---
    Exemple de la page « ErrorNotFound ».
    ```
    * Il s'agit d'un composant prédéfini dans {index}`Quasar` qui fournit une page d'erreur par défaut avec un message d'erreur 404. La page a été adaptée au design du site afin que son apparence soit plus agréable et cohérente.  
- src/pages/IndexPage.vue
    * Cette page est la page principale du site. Elle affiche, grâce au composant « LayerPostComment », toutes les publications. La page contient 4 options d’affichage. Voici le code pour le filtrage des publications :
    ```{literalinclude} project/src/pages/IndexPage.vue
    :language: html
    :caption: src/pages/IndexPage.vue
    :linenos: true
    :lines: 60-106
    ```
    * Cette méthode de filtrage est assez intuitive. Lorsque le site est lancé, la variable « filteroptiontype » est égale à « null », ce qui signifie qu'aucun filtre n'est activé. Par conséquent, toutes les publications s'affichent, triées par ordre chronologique. Voici un exemple de page:
    ```{figure} figures/Index_page_exemple.png
    ---
    width: 50%
    ---
    Exemple de la page "IndexPage".
    ``` 
    * Au moment où l’utilisateur appuie sur un profil dans une publication, la variable « filteroptiontype » se voit attribuer la valeur « name ». La fonction assigne alors à la variable « UpdatedList » la liste des publications qui ont été rédigées  par la personne choisie. C’est la même logique quand l’utilisateur appuie sur une branche: La fonction fait le filtrage par rapport aux publications qui ont cette même branche en commun. De plus, cette fonction permet également d'afficher les publications que l'utilisateur suit lorsque l'utilisateur clique sur le bouton « suivies ».
    * Finalement, la dernière partie importante de cette page est sa pagination. Elle possède une pagination réactive, qui augmente lorsque des publications sont ajoutées. Un nombre de 5 publications est affiché au maximum par page. Au bas du site se trouve une pagination qui permet de voir toutes les publications publiées.

- src/pages/LogInPage.vue
    * La page "LogInPage" est la première page que l’utilisateur voit. C’est un formulaire fictif, car ce n’est pas réellement une création de compte, mais une manière de pouvoir avoir les noms des utilisateurs lors de la création d’une publication ou d’un commentaire. Voici ce que le site affiche.
    ```{figure} figures/exemple_page_login.png
    ---
    width: 50%
    ---
    Exemple de la page "LogInPage".
    ```
    * La fonction principale est « controlTheValues() », qui empêche l'utilisateur de finaliser la connexion si des conditions ne sont pas remplies. Cette fonction vérifie si chaque champ est bien rempli et si le nom d'utilisateur ne dépasse pas la longueur maximale fixée à 20 caractères. Si l'une de ces conditions n'est pas respectée, un message s'affiche pour expliquer le problème rencontré. Lorsqu'il n'y a aucun problème, la page « IndexPage » s'ouvre.
- src/pages/settingsPage.vue
    * La page « Paramètres » est une page très utile pour l’utilisateur. Voici à quoi elle ressemble.
    ```{figure} figures/exemple_parametre.png
    ---
    width: 60%
    ---
    Exemple d'un page "settingsPage".
    ```
    * La première fonctionnalité est la possibilité de changer la photo de profil. Elle apparaît quand une publication est faite par l’utilisateur. Ensuite, un bouton « Supprimer les publications » permet de remettre les publications à zéro et d’afficher seulement les deux publications qui servent d’exemple. Finalement, le bouton « Se déconnecter » donne la possibilité à l’utilisateur de se déconnecter.
- src/router/index.js
    * Ce fichier est utilisé par les applications Vue.js dans le but de définir et de mettre en place le système de routage de l’application. 
-src/router/routes.js
    * Ce fichier-ci contient les informations sur les routes, comme les chemins URL. 
    ```{literalinclude} project/src/router/routes.js
    :language: html
    :caption: src/router/routes.js
    :linenos: true
    ```
    * Les routes {cite:p}`router` individuelles qui sont montrées ci-dessus en tant que « path » permettent de faire fonctionner tout le site et de charger les pages définies. Il y a la route principale qui est le chemin « / ». Ensuite, il y a les routes « enfant », comme "IndexPage" et "settingsPage", qui sont chargées à l’intérieur du composant MainLayout. La dernière route est un « attrape tout », ce que signifie qu’elle est utilisée pour toutes les routes non définies.
- src/stores/comment.js
    * Ce {index}`store` est une bibliothèque de gestion d'états qui est dédiée aux publications. Il permet le stockage de données, ainsi que la création de fonctions globales. Ce {index}`store` commence par les variables globales, qui peuvent être appelées dans tout le projet.  
    * Le {index}`store` contient ensuite la fonction « loadComment ». Si cette fonction est définie avec le paramètre « localStorage », les publications sont chargées dans la variable « commentsList » depuis le "local Storage" lors de l’ouverture de la page « IndexPage ». S’il n’y a aucune publication dans le "localStorage", des publications déjà préparées, sont enregistrées dans la variable ci-dessus et dans le "localStorage".  Le paramètre «localStorage » permet de faciliter le codage lors de la création d’un backend, car il suffit de changer le paramètre « location » par « backend ».
    * La fonction « addComment » prend plusieurs paramètres en compte. Voici un bout de la fonction :
    ```{literalinclude} project/src/stores/comment.js
    :language: html
    :caption: src/stores/comment.js
    :linenos: true
    :lines: 89-105
    ```
    * Cette fonction prend la variable « type » comme premier paramètre. Cette variable permet de définir si la fonction ajoute un commentaire ou une publication. Ensuite, la variable « id » permet de savoir dans quelle publication le commentaire doit être ajouté. Cependant, lors de l’ajout d’une publication, elle n’est d’aucune utilité. La variable « comment » est définie sur les pages de l’appel de la fonction. Elle contient les informations, comme la description écrite si c’est une création de commentaire. Si c’est une création de publication, elle contiendra en plus le titre et la branche. Les variables « nameprofile » et « pp_profile » sont définies lors de l’appel de la fonction avec l’utilisation du {index}`store` utilisateur. Puis toutes les informations sont ajoutées dans l’objet "comment". Finalement, les conditions « if » suivantes permettent de définir la liste sur laquelle on veut travailler. Lorsque l’utilisateur veut ajouter un commentaire, la fonction définit « this.commentstomodify », qui contient les commentaires de la publication choisie et qui permet de trouver l’id du nouveau commentaire à ajouter. Si l’utilisateur veut ajouter une publication, « this.commentstomodify » est défini comme la liste de toutes les publications, car cette fois il faut trouver l'id de la nouvelle publication. 
    * La partie suivante permet de trouver l'id du commentaire ou de la publication.
    ```{literalinclude} project/src/stores/comment.js
    :language: html
    :caption: src/stores/comment.js
    :linenos: true
    :lines: 106-117
    ```
    * Tout d’abord, la clé « id » dans l’objet « comment » reçoit comme valeur 0. Puis, la première condition contrôle la taille de la liste. Si la liste est vide, l'id sera d’office 0. Si la liste n’est pas vide, une boucle compare l'id des publications ou des commentaires présents.  Lorsque l’id de l'objet est plus grand que l’id du nouveau commentaire ou de la nouvelle publication, l’id de l'objet est défini par l’id trouvé + 1. Après avoir traversé toute la liste, l’id recherché est défini. 
    * La dernière partie permet d’enregistrer la nouvelle publication ou le nouveau commentaire.
    ```{literalinclude} project/src/stores/comment.js
    :language: html
    :caption: src/stores/comment.js
    :linenos: true
    :lines: 119-133
    ```
    * Comme montré ci-dessus, le code a deux manières de définir la variable « commentsList ». Si c’est un commentaire, le nouveau commentaire est ajouté dans la bonne publication, et si c’est une publication, celle-ci est ajoutée dans la liste des publications. Pour finir, la nouvelle liste est ajoutée dans le localStorage, car la variable location est « localStorage ».
    * La fonction suivante est nommée « deleteComment ». Elle prend en paramètres l'id de la publication que l'utilisateur souhaite supprimer et la destination, c'est-à-dire le local Storage. Avant de s'exécuter, elle demande une confirmation à l'utilisateur, puis offre la possibilité de supprimer la publication sélectionnée.
    * La dernière fonction « resetComment » prend en paramètre la destination, qui est définie comme « localStorage ». Elle efface la variable contenant les listes des publications dans le localStorage.

- src/stores/index.js
    * Ce fichier permet d'intégrer le {index}`magasin` de {index}`Pinia`. 
- src/stores/user.js
    * Ce {index}`store` est utilisé afin de gérer les données relatives à l’utilisateur. Il contient par exemple la liste « followed » qui garde l’id des publications suivies.
    * Ce {index}store contient en premier lieu deux fonctions opposées. La fonction « loginVariable » prend en paramètre « location », qui correspond à l'endroit où les données sont recherchées, en l'occurrence le local Storage. Cette fonction a pour rôle de fermer la page « LogInPage », d'enregistrer les données de l'utilisateur dans le localStorage, de stocker la photo de profil par défaut dans le localStorage, et enfin, d'ouvrir la page « Indexpage ». La fonction opposée, « logOut », permet à l'utilisateur de se déconnecter et ouvre la page « LogInPage ». Elle utilise le même paramètre « location ».
    * Ensuite, il y a une fonction « changePpProfile». Cette fonction change la photo de profil de l’utilisateur par l’URL fournie dans le paramètre « NewLink ». Cette URL s’enregistre ainsi dans le localStorage.
    * La fonction la plus importante dans ce {index}`store` est la fonction «profileload ». Cette fonction charge les données de l’utilisateur dans toutes les pages. Voici la fonction :
    ```{literalinclude} project/src/stores/user.js
    :language: html
    :caption: src/stores/user.js
    :linenos: true
    :lines: 50-61
    ```
    * Cette fonction se lance lorsque l’utilisateur charge une page. Elle prend les données depuis le profil enregistré dans le localStorage. Si cette variable du localStorage est vide, la page « LogInPage » s’ouvre directement, ainsi l’utilisateur peut fournir les données. Cependant, si la variable contient les informations sur l'utilisateur, les variables globales sont définies grâce au localStorage.

- src/App.vue
    * Ce fichier est le point d'entrée de toute l’application {index}`Quasar`.
- .editorconfig {cite:p}`editorConfig`
    * Ce fichier définit les styles de codage et les conventions à utiliser dans les éditeurs. Il maintient la cohérence du projet.
- .eslintignore
    * Ce fichier est utilisé afin d’ignorer des fichiers spécifiques.
- .eslintrc.js {cite:p}`Eslint`
    * Ce fichier configure les règles ESLint, qui permettent aussi de garder une cohérence dans le projet.
- .gitignore {cite:p}`gitignore_gitkeep`
    * Ce fichier définit les fichiers qui ne doivent pas être suivis par Git.
- .gitpod.yml
    * Ce fichier permet de configurer l'environnement de développement dans Gitpod.
- .prettierrc
    * Ce fichier permet de formater le code en utilisant Prettier. Il assure un formatage automatique en fonction d’un ensemble de règles.
- .stackblitzrc
    * Ce fichier de configuration {index}`StackBlitz` permet de définir des paramètres, des dépendances et des préférences. 
-index.html
    * Ceci est le fichier {index}`HTML` principal. 
- jsconfig.json {cite:p}`jsconfig`
    * Ce fichier est utilisé pour configurer {index}`Javascript` dans {index}`Visual Studio Code`.
- package-lock.json
    * Ce fichier spécifie la version exacte à installer pour chaque dépendance.
- package.json
    * Ce fichier fournit toutes les dépendances à installer.
- postcss.config.js
    * Ce fichier configure PostCSS. 
- quasar.config.js {cite:p}`quasar-docs`
    * Ce fichier configure {index}`Quasar`, par exemple les paramètres, les thèmes, les plugins, etc…
- Read.me
    * Ce fichier contient des informations importantes sur le projet. Il est utile pour les utilisateurs et les développeurs, car il permet de comprendre rapidement le code. Il comporte un bref résumé du programme, les instructions pour l’installation et la mise en route du projet. Puis, il décrit aussi la manière d'utiliser le programme. 
- Yarn.lock
    * Ce fichier est créé par Yarn. L’objectif de ce fichier est de permettre aux développeurs d’utiliser la même version de chaque dépendance, évitant les problèmes.

