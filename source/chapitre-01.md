# Outils utilisés pour la création du projet


## Modélisation du front-end

Le premier outil utilisé afin de commencer le projet est Figma. Figma {cite:p}`Figma` est un outil de conception qui permet d’élaborer des interfaces utilisateur pour les sites Web et les applications mobiles. Il est conçu pour optimiser le processus de création pour des équipes de toutes tailles, réduisant ainsi le temps et les efforts nécessaires à la conception et au développement de produits numériques de haute qualité.

Dans le but de créer un site Web agréable et intéressant, le design UX {cite:p}`ux_design`, connu sous le nom de design utilisateur, est l’un des facteurs les plus importants à prendre en compte. Cela consiste en la conception de produits numériques en mettant l’accent sur l’expérience utilisateur. Il faut mettre à disposition des outils et une interface intuitive et facile à utiliser en vue de satisfaire les besoins des utilisateurs. Le prototypage du projet est alors primordial afin d’établir tous les points importants pour le projet. Ce projet étant réalisé dans l’intention d’être utilisé par les étudiants, il se doit d’avoir toutes les fonctionnalités potentiellement utiles.
   
```{figure} figures/comparaison.png
---
width: 30%
---
Comparaison avec le site Quora {cite:p}`Quora`
```

Pour la création du modèle, le site Quora a été utilisé comme inspiration. Quora {cite:p}`Quora1,Quora2` étant une plateforme de questions-réponses, elle s’adapte exactement au but du projet. Les points importants ont vite été repérés. Par exemple, il s’agissait de faire un site sombre qui s’adapte plus à l’usage quotidien ou encore un onglet accessible de façon à accéder facilement au groupe de branche. Un travail minutieux et complet a été effectué sur la modélisation afin d’avoir une base solide qui pourra être utilisée pendant toute la partie de programmation, comme la modélisation d'un site responsive qui peut s'adapter à tout type d'appareil.

```{admonition} Vous pouvez accéder à la maquette en annexe à ce rapport. En vue de voir la maquette complète, elle est présente sur la version HTML du rapport écrit.
```


## Programmation du projet

Pour la création d’un projet, l’utilisation d’outils, de frameworks et de bibliothèques est nécessaire afin de faciliter le codage.

### Outils de programmation

Premièrement, le projet est stocké sur {index}`GitHub`. {index}`GitHub` {cite:p}`Github` est une plateforme Web basée sur le cloud. Elle donne la possibilité de contrôler les versions du code et de développer collaborativement des logiciels qui permettent aux utilisateurs de partager leur code avec d'autres. Il offre une variété de fonctionnalités, telles que le suivi des problèmes ou les révisions de code, qui facilitent la collaboration entre les développeurs. 

Il est particulièrement intéressant d’utiliser {index}`StackBlitz` {cite:p}`StackBlitz1,StackBlitz2` qui est un environnement de développement en ligne pour la création d’applications Web. {index}`StackBlitz` est intégré dans le Cloud ce qui permet aux développeurs d’écrire, de tester et de déboguer leur code dans le navigateur. Il prend en charge un large éventail de technologies de {index}`développement Web`, notamment {index}`Javascript`, {index}`Vue.js`, un framework utilisé.

L’une des principales caractéristiques de {index}`StackBlitz` est la possibilité d’exécuter des applications dans le navigateur, ce qui signifie que les développeurs peuvent voir leurs modifications en temps réel sans avoir à configurer un environnement de développement local. Cela le rend particulièrement utile pour le prototypage rapide et le développement de petits projets. De plus, {index}`StackBlitz` offre une option pour partager et héberger facilement des applications. Ceci est utile pour faire tester des applications à d’autres personnes. Tout en étant possible d’intégrer {index}`GitHub`, il est alors le meilleur environnement pour ce projet de travail de maturité.

Ensuite, {index}`Vue.js` {cite:p}`VueJS1,VueJS2` est un framework {index}`Javascript` pour la création d’interfaces utilisateur et d’applications monopages. {index}`Vue.js` utilise une architecture basée sur des composants, qui permet aux développeurs de créer des éléments d’interface utilisateur réutilisables, modulaires et autonomes. Chaque composant définit ses propres données, méthodes et modèles, qui peuvent être facilement composés et réutilisés dans l’application. L’une des principales caractéristiques de {index}`Vue.js` est son système de réactivité, qui met automatiquement à jour l’interface utilisateur lorsque l’état du composant change. Cela facilite la création d’applications dynamiques et réactives qui se mettent à jour en temps réel.

Le framework {index}`Quasar` {cite:p}`Quasar,QuasarIntro` est aussi utilisé et permet de composer des interfaces utilisateur réactives et performantes avec {index}`Vue.js`. {index}`Quasar` est conçu pour fonctionner de manière intuitive avec {index}`Vue.js`. Il comprend un ensemble de fonctionnalités dans le but d’aider les développeurs à créer des applications Web et mobiles avec une apparence cohérente. Ce framework comprend un riche ensemble de composants d’interface utilisateur, d’utilitaires et de directives prédéfinies. {index}`Quasar` est particulièrement utile pour créer des applications réactives qui s’affichent et se comportent de manière cohérente sur différents appareils et tailles d’écran.

### Stockage des données

{index}`Pinia` {cite:p}`pinia,pinia2` aide à gérer les données d'une application {index}`Vue.js` en fournissant un modèle de {index}`magasin` ou de {index}`store` qui permet de définir et d’accéder aux données à partir de n’importe quel composant de l’application. {index}`Pinia` donne la possibilité de créer un {index}`magasin` avec des propriétés réactives et des méthodes pour les manipuler. Il est possible d’ajouter des actions, qui sont des méthodes permettant d’effectuer des fonctions. L’un des principaux avantages de {index}`Pinia` est sa réactivité. Chaque fois que l’état change, {index}`Pinia` met automatiquement à jour tous les composants qui en dépendent, garantissant ainsi que l’interface utilisateur soit toujours synchronisée avec les données.

### Écriture de la documentation

Sphinx {cite:p}`sphinx1,sphinx2` est un outil utilisé pour documenter les projets logiciels. Cet outil peut générer de la documentation dans différents formats, en particulier les formats {index}`HTML` et PDF sont supportés et utilisés dans le cadre de ce projet. Sphinx utilise le langage de balisage reStructuredText (RST) afin d’annoter des documents textuels avec des symboles sémantiques, par exemple pour indiquer des titres, des énumérations, etc…  Grâce à ce langage de balisage, qui est à la fois facile à lire et à écrire, des outils de conversion spécialisés permettent une mise en page automatique et intuitive.
