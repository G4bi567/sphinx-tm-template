# Outils utilisés pour la création du projet


## Modélisation du front-end

Le premier outil utilisé afin de commencer le projet est Figma. Figma {cite:p}`Figma` est un outil de conception qui permet d’élaborer des interfaces utilisateur pour les sites Web et les applications mobiles. Il vise à faciliter la création sur les interfaces pour les équipes de toutes tailles, réduisant ainsi le temps et les efforts nécessaires à la conception et au développement de produits numériques de haute qualité.

Dans le but de créer un site Web agréable et intéressant, le design UX {cite:p}`ux_design`, connu sous le nom de design utilisateur, est l’un des facteurs les plus importants à prendre en compte. Cela consiste en la conception de produits numériques en mettant l’accent sur l’expérience utilisateur. Il faut mettre à disposition des outils et une interface intuitive et facile à utiliser en vue de satisfaire les besoins des utilisateurs. Le prototypage du projet est alors primordial afin d’établir tous les points importants pour le projet. Ce projet étant réalisé dans l’intention d’être utilisé par les étudiants, il se doit d’avoir toutes les fonctionnalités potentiellement utiles.
   
```{figure} figures/comparaison.png
---
width: 30%
---
Comparaison 
```

Pour la création du modèle, le site Quora a été utilisé comme inspiration. Quora {cite:p}`Quora1,Quora2` étant une plateforme de questions-réponses, elle s’adapte exactement au but du projet. Les points importants ont vite été repérés. Par exemple, il s’agissait de faire un site sombre qui s’adapte plus à l’usage quotidien ou encore un onglet accessible de façon à accéder facilement au groupe de branche. Un travail minutieux et complet a été effectué sur la modélisation afin d’avoir une base solide qui pourra être utilisée pendant toute la partie de programmation.

```{admonition} Vous pouvez accéder à la maquette en annexe à ce rapport. En vue de voir la maquette complète, elle est présente sur la version HTML du rapport écrit.
```


## Programmation du projet

Pour la création d’un projet, l’utilisation d’outils, de framework et de bibliothèques est nécessaire afin de faciliter le codage.

### Outils de programmation

Premièrement, le projet est stocké sur GitHub. GitHub est une plateforme web de contrôle de version et de développement collaboratif de logiciels qui permet aux utilisateurs d'héberger, de gérer et de partager leur code avec d'autres. Il offre une variété de fonctionnalités, telles que le suivi des problèmes ou les révisions de code, qui facilitent la collaboration entre les développeurs. 

Il a été proposé d’utiliser StackBlitz qui est un environnement de développement en ligne pour la création d’applications Web. Il s’agit d’un environnement de développement intégré (IDE) dans le Cloud qui permet aux développeurs d’écrire, de tester et de déboguer leur code dans le navigateur. Il prend en charge un large éventail de technologies de développement Web, notamment JavaScript, Angular, React et surtout Vue.js, qui est un composant important dans la solution retenue.

L’une des principales caractéristiques de StackBlitz est la possibilité d’exécuter des applications dans le navigateur, ce qui signifie que les développeurs peuvent voir leurs modifications en temps réel sans avoir à configurer un environnement de développement local. Cela le rend particulièrement utile pour le prototypage rapide et le développement de petits projets. De plus, StackBlitz offre une option pour partager et héberger facilement des applications. Ceci est utile pour faire tester des applications à d’autres personnes. Tout en étant possible d’intégrer GitHub, il est alors le meilleur environnement pour ce projet de travail de maturité.

Ensuite, Vue.js est un framework JavaScript pour la création d’interfaces utilisateur et d’applications monopages. Vue.js utilise une architecture basée sur des composants, qui permet aux développeurs de créer des éléments d’interface utilisateur réutilisables, modulaires et autonomes. Chaque composant définit ses propres données, méthodes et modèles, qui peuvent être facilement composés et réutilisés dans l’application. L’une des principales caractéristiques de Vue.js est son système de réactivité, qui met automatiquement à jour l’interface utilisateur lorsque l’état du composant change. Cela facilite la création d’applications dynamiques et réactives qui se mettent à jour en temps réel.

Le framework Quasar est aussi utilisé et permet de composer des interfaces utilisateur réactives et performantes avec Vue.js. Quasar est conçu pour fonctionner de manière intuitive avec Vue.js. Il comprend un ensemble de fonctionnalités dans le but d’aider les développeurs à créer des applications Web et mobiles avec une apparence cohérente. Ce framework comprend un riche ensemble de composants d’interface utilisateur, d’utilitaires et de directives prédéfinies. Quasar est particulièrement utile pour créer des applications réactives qui s’affichent et se comportent de manière cohérente sur différents appareils et tailles d’écran.

### Stockage des données

Pinia aide à gérer les données d'une application Vue.js en fournissant un modèle de magasin qui permet de définir et d’accéder aux données à partir de n’importe quel composant de l’application. Pinia donne la possibilité de créer un magasin avec des propriétés réactives et des méthodes pour les manipuler. Il est possible d’ajouter des actions, qui sont des méthodes permettant d’effectuer des fonctions. L’un des principaux avantages de Pinia est sa réactivité. Chaque fois que l’état change, Pinia met automatiquement à jour tous les composants qui en dépendent, garantissant ainsi que l’interface utilisateur soit toujours synchronisée avec les données.

### Écriture de la documentation

Sphinx est un outil utilisé pour documenter les projets logiciels. Cet outil peut générer de la documentation dans différents formats, en particulier les formats HTML et PDF sont supportés et utilisés dans le cadre de ce projet. Sphinx utilise le langage de balisage reStructuredText (RST) afin d’annoter des documents textuels avec des symboles sémantiques, par exemple pour indiquer des titres, des énumérations, etc…  Grâce à ce langage de balisage facile à lire et à écrire, des outils de convertion spécialisés font la mise en page automatiquement et intuitivement.
