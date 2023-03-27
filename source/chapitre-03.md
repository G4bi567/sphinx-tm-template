# Guide et documentation développeur 
## Structure du code et rôle des fichiers
Dans ce sous-chapitre, il y a une analyse approfondie sur tous les fichiers du projet.

- src/boot/.gitkeep
    * Ce fichier n’est pas un fichier spécifique à Quasar, mais un fichier ajouté par Git. Il permet d’inclure des répertoires vides dans le dépôt du projet afin de donner des instructions aux codeurs.
- src/components/CreatePost.vue
    * Le composant permet à l’utilisateur de poser une question, c’est à dire de créer sa publication. Ce composant permet de recueillir des données. 
    ```{figure} figures/CreatePost_composant.png
    ---
    width: 30%
    ---
    Exemple du composant « CreatePost ». 
    ```
    * Tout d’abord, l’utilisateur doit fournir la branche sur laquelle il a un questionnement. Puis il doit écrire un titre pour sa publication. Finalement, il doit rédiger la description du problème, en vue de faire comprendre le mieux possible le problème aux autres utilisateurs. La description peut être complète grâce aux options de police et de format de la description. Le composant se termine par un bouton de soumission « Envoyer » qui permet d’activer la fonction qui enregistre la publication. Puis l’utilisateur est envoyé sur la page d’accueil avec la nouvelle publication présente. La fonction « addPost » qui permet d’enregistrer la nouvelle publication sera mieux expliquée dans src/stores/comment.js.
    * Une fonctionnalité intéressante sur ce composant serait la fonction « isAvailable ». 
    
     ```{figure} figures/Fonction_isAvailable.png
    ---
    width: 30%
    ---
    La fonction « isAvailable ». 
    ```
    * Lors de la création de la publication, il faut absolument que les 3 entrées soit remplies. Cette fonction permet de bloquer les actions lorsque le bouton de soumission est activé. Elle active la variable du store isAvailableVar, en affectant la valeur false. Cette variable commence par empêcher le changement de page, lors de l’appel la fonction « $emit('finished') » et affiche une phrase « il manque au moins une entrée ». Si toutes les conditions sont respectées, toutes les actions seront effectuées
- src/components/LayerPostComment.vue
    * Le composant actuelle permet de créer un modèle pour les publications et pour les commentaires. 
     ```{figure} figures/comment.png
    ---
    width: 40%
    ---
    Exemple du composant « CreatePost ». 
    ```
    * Ce composant prend en paramètre les données fournies par le composant « CreatePost.vue », vu précédemment. Premièrement, Il affiche, sur la partie supérieure droite, la photo de profil et le nom de l’utilisateur. Cette partie est cliquable et permet d’envoyer l’utilisateur dans la page du profil cliqué. Ensuite, sur la partie supérieure gauche, un menu déroulant est présent. Lorsque ce menu est cliqué, une option « supprimer » apparaît. Celle-ci donne la possibilité de supprimer la publication. Puis, la partie du centre est composé du nom de la branche, du titre de la publication et la description du problème. Le nom de la branche est cliquable et emmène l’utilisateur dans une page dédiée aux publications avec la branche choisie. Sur la partie inférieure, se trouve des fonctionnalités plus interactives. Tout d’abord, un bouton affiche la partie des commentaires. Puis, un bouton cœur permet d’enregistrer une publication dans les suivis. 
    ```{figure} figures/comment_partie_commentaire.png
    ---
    width: 40%
    ---
    Exemple du composant « CreatePost ». 
    ```
    * Avec la nouvelle partie, affichée ci-dessus, les personnes, voulant répondre à la publication, peuvent créer un commentaire. Il suffit d’écrire la résolution du problème. Puis, grâce au bouton « répondez », le commentaire est ajouté dans le site. 
    * La spécialité de ce composant est qu’il est récursif. Un composant récursif est un composant qui s’appelle elle-même. Ainsi dans cette situation, cela permet de faire des publications avec des commentaires qui ont des commentaires, etc… Voici un schéma pour mieux comprendre les fonctions récursives.
    ```{figure} figures/Diagramme_recursive.png
    ---
    width: 40%
    ---
    Exemple du comment.vue
    ```
    * Grâce à la récursivité, il n’y a pas besoin d’avoir d’autres composants modèle. Les commentaires des publications n’ont pas de titres et de branches, mais grâce à des conditions, c’est possible de garder toujours le même composant.
- src/scss/app.scss
    * Un fichier scss contient les styles, en CSS, pour l’ensemble de l’applications. C’est-à-dire des styles globaux qui pourront être utilisés dans tout le code. Il est automatiquement créé par Quasar, lors de la création d’un nouveau projet Quasar.
- quasar.variables.scss
    * Ce fichier-ci permet de créer des variables qui sont utilisées pour la personnalisation des composants. Il est aussi automatiquement généré par la création d’un nouveau projet Quasar. 
- src/layouts/MainLayout.vue
    * Le MainLayout est la base du projet. Ce fichier consiste visuellement en la barre de navigation, affichée en haut du site. 
    ```{figure} figures/MainLayout.png
    ---
    width: 60%
    ---
    Exemple du MainLayout.vue
    ```

    
    * Cette barre permet d’accéder à plusieurs fonctionnalités du site. Tout d’abord, des boutons « Home page » et « Suivis » sont présents. Ils permettent d’accéder soit à la page principale des publications soit à la page réservée aux publications suivies. Le bouton « Home Page » sert à remettre à zéro la page lorsqu’un filtre est utilisé. La page suivis est utile à l’utilisateur, en vue de vouloir voir l’évolution de la discussion pour résoudre un problème. Ensuite, une image du logo du Collège du Sud et « Forum CSUD » font office de titre pour le site Web. Puis, un bouton « une question », il permet d’accéder au formulaire de création de publication, vu précédemment comme étant le composant « CreatePost ». Finalement, il y a un menu déroulable qui permet d’accéder à la page des paramètres du site.
    * Deux autres boutons sont sur les extrémités. Ils permettent d’ouvrir des « drawers », c’est-à-dire des tiroirs montrés ci-dessous:
    ```{figure} figures/exemple_tiroir_branche.png
    ---
    width: 20%
    ---
    Exemple du tiroir des branches
    ```
    * Du côté gauche, les branches de publications sont affichées. Lorsque l’utilisateur clique sur une des branches, il est amené sur la page de la branche et ne peut alors voir que les publications dont la branche est la même. Cependant du côté droite, des liens utilises pour les étudiants sont affichés. Il est important de fournir des outils aux élèves.
    * La suite du code permet d’afficher alors les composants et les pages principales du site. Cette fonctionnalité est établie grâce à des conditions qui dépendent de variables qui changent lorsque l’utilisateur accède aux pages du site.
    ```{figure} figures/router_filtre.png
    ---
    width: 40%
    ---
    Code pour faire apparaître les pages
    ```
    * L’affichage de la page principale varie principalement entre 3 pages.
    * Tout d’abord, la page de Login. Cette page est la première page à s’afficher pour un nouvel utilisateur. Le site n’ayant aucune information sur le profil, la variable login sera fausse et ainsi permettre à la page « LogInPage » d’apparaître. Une fois le formulaire de connexion rempli, la variable sera égale à vrai. Alors s’affiche la deuxième page, c’est-à-dire le fil des récentes publications dans l’ordre de publication. Cette page est faite grâce à « IndexPage.vue ». Puis, si l’utilsateur décide d’écrire une question, en appuyant sur le bouton une question, la variable « writeComment » est égal à true. Ainsi le composant « CreatePost » apparaît. Une fois le formulaire rempli, la variable est affectée à false et s’affiche la page de fil des publications.

- src/pages/ErrorNotFound.vue
    * La page « ErrorNotFound.vue » est un page qui s’affiche lorsque l’utilisateur essaye d’ouvrir une page qui n’existe pas. Lors de cette situation, il est affiché une erreur 404, qui est une erreur qui signifie que la route url n’existe pas. 
    * Voici le design de celle si : 
    ```{figure} figures/error_page.png
    ---
    width: 40%
    ---
    Code pour faire apparaître les pages
    ```
    * Il s'agit d'un composant prédéfini dans Quasar qui fournit une page d'erreur par défaut avec un message d'erreur 404. La page a été adaptée au design de tout le site afin que l’utilisation soit plus agrèable. 
- src/pages/IndexPage.vue
    * Cette page est la page principale du site. Elle affiche, grâce au composant « LayerPostComment.vue », toutes les publications. La page contient 4 options d’affichage. Voici le code pour le filtrage des publications :
    ```{figure} figures/fonction_filtrage_publication.png
    ---
    width: 40%
    ---
    Code pour filtrer toutes les publications
    ```
    * Cette méthode de filtrage est assez facile à comprendre. Lorsque le site se charge la variable « filteroptiontype » est égal à null, alors il va s’afficher toutes les publications triées dans l’ordre chronologique, car il n’y a aucun filtre activé. Voici un exemple de la page sans filtre.
    ```{figure} figures/Index_page_exemple.png
    ---
    width: 40%
    ---
    Exemple de la page "IndexPage"
    ``` 
    * Au moment où l’utilisateur appuie sur un profil dans un publication, la variable « filteroptiontype » est alors assignée à « name ». La fonction assignera à la variable « UpdatedList » la liste des publications qui ont été écrites par la personne choisie. C’est la même logique quand l’utilisateur appuie sur une branche, la fonction, cette fois-ci, fait le filtrage par rapport aux publications qui ont cette même branche en commun. En plus, la fonction permet aussi de faire afficher les publications qu’on a voulus suivre, lorsque l’utilisateur appuie sur le bouton « Suivis ».

    * Finalement, la dernière partie importante de cette page est sa pagination. Elle possède une pagination réactive, qui augmente lorsque des publications sont ajoutées. Un nombre de 5 publications est affiché au maximum par page. Au bas du site, se trouve une pagination qui permet de voir toutes les publications publiées.

- src/pages/LogInPage.vue
    * La page LogIn est la première page que l’utilisateur voit. C’est un formulaire fictif, car ce n’est pas réellement une création de compte, mais une manière de pouvoir avoir les noms des utilisateurs lors de la création d’une publication ou d’un commentaire. Voici ce que le site affiche.
    ```{figure} figures/exemple_page_login.png
    ---
    width: 40%
    ---
    Exemple de la page "LogInPage"
    ```
    * La fonction principale est la « controlTheValues() » qui empêche à l’utilisateur de finir la connexion avec des champs d’entrée vides. Cette fonction contrôle chaque champ pour savoir s’il est rempli, si au moins n’est pas rempli, un message apparaît expliquant qu’il manque au moins une entrée. Lorsqu’il n’y a aucun problème, la page IndexPage s’ouvre.
- src/pages/settingsPage.vue
    * La page paramètre est une page très utile pour l’utilisateur. Voici à quoi elle ressemble.
    ```{figure} figures/exemple_parametre.png
    ---
    width: 40%
    ---
    Exemple d'un page "settingsPage"
    ```
    * La première fonctionnalité est la possibilité de pouvoir changer la photo de profil, elle apparaît quand une publication est faite par l’utilisateur. Ensuite, un bouton « supprimer les publications » permet de remettre les publications à zéro et d’afficher seulement les deux publications , qui servent comme exemple. Finalement, le bouton « Se déconnecter » donne la possibilité à l’utilisateur de se déconnecter dans le but de se connecter afin de changer de nom.
- src/router/index.js
    * Ce fichier est utilisé par les applications Vue.js dans le but de définir et mettre en place le système de routage de l’application. 
-src/router/routes.js
    * Ce fichier-ci contient les informations sur les routes, comme les chemins Url. 
    ```{figure} figures/code_router.png
    ---
    width: 50%
    ---
    Voici le code dans le fichier
    ```
    * Les itinéraires individuels, qui sont montrées ci-dessus en tant que « path », permettent de faire fonctionner tout le site et chargé les pages fournies. Il y a la route principale qui est le chemin « /». Ensuite, il y a les routes « enfant », comme « IndexPage » et « settingsPage », qui sont chargés à l’intérieur du composant « MainLayout ». La dernière route s’agit d’un route « attrape tout », ce que signifie qu’elle est utilisée pour les routes qui ne correspondent à aucune fournit.
- src/stores/comments.js
    * Ce store est une bibliothèque de gestion état qui est dédiée aux publications. Il permet un stockage de données, et aussi la création de fonction globale. Ce store commence par les variables globales, elles peuvent être appelées dans tout le projet.  
    * Le store contient ensuite la fonction « loadComment ». Si cette fonction est définit avec le paramètre « localStorage », elle permet lors de l’ouverture de la page « IndexPage » de charger les publications dans la variable « commentsList » qui sont stockées dans le local Storage. S’il n’y aucune publication dans le local Storage, des publications ,qui sont déjà faites, sont enregistrer dans la variable ci-dessus et dans le local Storage.  Le paramètre «localStorage » permet lors de la création d’un backend de faciliter le codage, car il faudrait juste changer le paramètre « location » par « backend ».
    * La fonction suivante « addComment » prend plusieurs paramètres en compte. Voici un bout de la fonction :
    ```{figure} figures/partie_1_addComment.png
    ---
    width: 40%
    ---
    Voici la première partie du code dans la fonction «addComment»
    ```
    * Cette fonction prend pour commencer la variable « type ». Cette variable permet de définir si la fonction ajoute un commentaire ou une publication. Ensuite, la variable « id » est utile pour l’ajout d’un commentaire car elle permet de savoir dans quelle publication le commentaire doit être ajoutée. Cependant lors de l’ajout d’une publication, elle n’est d’aucune utilité. La variable « comment » est définit sur les pages de l’appel de la fonction. Elle contient les informations, comme la description écrite si c’est une création de commentaire. Si c’est une création de publication, elle contiendra en plus le titre et la branche. Les variables « nameprofil » et « pp_profil » sont définies lors de l’appel de la fonction avec l’utilisation du store utilisateur. Puis toutes les informations sont ajoutées dans l’object comment. Finalement, les conditions « if » suivantes permettent de définir la liste sur laquelle on veut travailler. Lorsque l’utilisateur veut ajouter un commentaire, la fonction définit « this.commentstomodify » en tant que les commentaire de la publication choisie , dans le but de de trouver l’id du nouveau commentaire à ajouter. Si cette fois l’utilisateur veut ajouter une publication, « this.commentstomodify » est définit comme la liste de toutes le publications, car cette fois il faut trouver quelle id il faut donner à la nouvelle publications. 
    * La partie suivante permet de trouver le id du commentaire ou de la publication.
    ```{figure} figures/partie_2_addComment.png
    ---
    width: 40%
    ---
    Voici la deuxième partie du code dans la fonction «addComment»
    ```
    * Tout d’abord, la clé « id » dans l’object « comment » reçoit comme valeur 0. Puis, la première condition contrôle la taille de la liste. Si la liste est vide, le id sera d’office 0. Sinon, lorsque la liste n’est pas vide, une boucle compare le id des publications ou des commentaires présents.  Lorsque l’id est plus grand que l’id du nouveau commentaire ou de la nouvelle publication, l’id de la nouvelle publication ou du nouveau commentaire est définit par l’id trouvé + 1. Après avoir traversé toute la liste, l’id recherché est définit. 
    * La dernière partie permet d’enregistrer la nouvelle publication ou le nouveau commentaire.
    ```{figure} figures/partie_3_addComment.png
    ---
    width: 40%
    ---
    Voici la troisième partie du code dans la fonction «addComment»
    ```
    * Comme montré ci-dessus, le code a deux manières de définir la variable « commentsList ». Si c’est un commentaire, le nouveau commentaire est ajouté dans la bonne publications, et si c’est un publication , celle-ci est ajoutée dans la liste des publications. Pour finir, la nouvelle liste est ajoutée dans le local Storage, car la variable location est « localStorage ».
    * La fonction suivante s’appelle « deleteComment ».  Celle-ci prend en paramètre le id de la publication que l’utilisateur veut supprimer et elle prend aussi la destination, c’est à dire le local Storage. Elle donne la possibilité de supprimer la publication choisie.
    * La dernière fonction « resetComment » prend en paramètre la destination, qui est définit comme « localStorage ». Elle efface la variable contenant les listes des publications dans le localStorage.

- src/stores/index.js
    * Ce fichier permet d'intégré le magasin de Pinia. 
- src/stores/utilisateur.js
    * Ce store est utilisé afin de gérer les données en rapport avec l’utilisateur. Il contient par exemple la liste « followed » qui garde l’id des publications suivies.
    * Pour les fonctions, ce store possède pour commencer deux fonctions opposées. La fonction « loginVariable » prend en paramètre « location » l’endroit où les données sont recherchées, ici le local Storage. Cette fonctionne permet premièrement de fermer la page « LogInPage », puis enregistre les données de l’utilisateur dans le local Storage. Finalement, elle enregistre la photo de profil de base dans le localStorage. Ensuite, la fonction opposée « logOut » qui donne la possibilité, cette fois-ci, d’effacer les données sur l’utilisateur et d’ouvrir la page « LogInPage ». Elle utilise le même paramètre « location ».
    * Ensuite, il y a une fonction « changePpProfil». Cette fonction change la photo de profil de l’utilisateur par l’url fournie dans le paramètre « NewLink », cette url s’enregistre ainsi dans le local Storage.
    * La fonction la plus importante dans ce store est la fonction «profilload ». Cette fonction charge les données de l’utilisateur dans toutes les pages. Voici la fonction :
    ```{figure} figures/code_profilLoad.png
    ---
    width: 40%
    ---
    Code de la fonction «profilload»
    ```
    * Lorsque l’utilisateur charge une page, cette fonction se lance. Elle prend les données sur le profil enregistrées dans le local Storage. Si cette variable est vide, la page « LogInPage » s’ouvre directement, ainsi l’utilisateur peut fournir les données. Sinon, les variables globales sont définies.

- src/App.vue
    * Ce fichier est la racine de toute l’application Quasar.
- .editorconfig
    * Ce fichier définit les styles de codage et les conventions à utiliser dans les éditeurs. Il maintient la cohérence du projet.
- .eslintignore
    * Ce fichier est utilisé afin d’ignorer des fichiers spécifiques.
- .eslintrc.js
    * Ce fichier configure les règles ESLint, qui permettent aussi de garder une cohérence dans le projet.
- .gitignore
    * Ce fichier définit les fichiers qui ne doivent pas être suivis par Git. 
- .prettierrc
    * Ce fichier permet de formatter le code en utilisant Prettier. Il assure un formatage automatique en fonction d’un ensemble de règles.
- .stackblitzrc
    * Ce fichier permet de configurer Stackblitz. Il permet d’assurer des paramètres, des dépendances et de préférences si nécessaire. 
-index.html
    * Ceci est le fichier HTML principale. 
- jsconfig.json
    * Ce fichier est utilité pour configurer Javascript dans Visual Studio Code.
- package-lock.json
    * Ce fichier spécifie la version exacte à installer pour chaque dépendances.
- package.json
    * Ce fichier fournit toutes les dépendances à installer.
- postcss.config.js
    * Ce fichier configure PostCSS. 
- quasar.config.js
    * Ce fichier configure Quasar, comme les paramètres, les thèmes, les plugins, etc…
- Read.me
    * Ce fichier contient des informations importantes sur le projet. Il est utile pour les utilisateurs et les développeurs, car il permet de comprendre rapidement le code. Il comporte un bref résumé du programme, les instructions pour l’installation et la mise en route du projet. Puis il possède aussi la manière de l’utiliser. 
- Yarn.lock
    * Ce fichier est créé par Yarn. L’objectif de ce fichier est de permettre aux développeurs d’utiliser la même version de chaque dépendance, évitant les problèmes.


