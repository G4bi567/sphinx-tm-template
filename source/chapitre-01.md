# Fonctionnement du projet

## Explication des composants utilisés

Comme dit précédemment, Vue.js utilise une architecture basée sur les composants. Il est donc utile d'utiliser cette fonctionnalité dès que possible pour éviter les répétitions et des codes trop longs.
### Composants de mise en page des publications
Les composants de mise en page définissent la structure et la disposition des informations données. Un des avantages de cette fonctionnalité est de pouvoir l'utiliser dans l'ensemble de l'application et ainsi maintenir une forme de cohérence et d'unité.
#### PostLayer

Ce composant fut le premier créé, il permet grâce à une array d'objets de faire une publication. L'array contient le titre de la publication, la date, le nom de profil du créateur, la description du problème, la branche associée au problème, la photo de profil du créateur, l'id de la publication qui permet de l'identifier et les commentaires sous forme de array. Vous pouvez voir un exemple de ce composant ci-dessous.

```{figure} figures/Exemple_Postlayer.png
---
width: 100%
---
Exemple du Postlayer 
```

Pour la partie supérieure du composant, la photo de profil et le nom de profil sont des objets cliquables qui permettent d'envoyer l'utilisateur dans la page de publication du créateur. Un bouton déroulable est aussi disponible afin de pouvoir supprimer les publications.

Ensuite, en bas, la branche de la publication est aussi cliquable et permet de nous diriger vers la page de celle-ci. 
Puis, comme vous pouvez le voir, le titre, la description et la date sont affichées. 

Finalement, nous avons un bouton commentaire qui ouvre la section des commentaires. Nous pouvons ainsi ajouter un commentaire à l'array. Les commentaires des autres utilisateurs sont également affichés et peuvent même être commentés. 

#### CommentLayer

Ce composant fonctionne comme le PostLayer sauf que je trouvais que les commentaires n'avaient pas besoin d'autant d'informations que celui-ci. En effet, l'array ne contient pas de titre, de branche. Vous pouvez voir un exemple de ce composant ci-dessous.

```{figure} figures/Exemple_CommentLayer.png
---
width: 100%
---
Exemple du CommentLayer 
```

Ce composant est récursif. Un composant récursif en Vue.js est un composant qui appelle lui-même de manière répétée. Cela peut être utile pour afficher des données hiérarchiques, telles que , ici, les commentaires des commentaires par exemple. Vous pouvez voir ici un diagramme qui explique comment fonctionne ce composant.

```{figure} figures/Diagramme_recursive.png
---
width: 100%
---
Exemple du CommentLayer 
```

### Composant pour créer une publication

#### CreatePost

Ce composant est utilisé pour créer une nouvelle publication. Il contient 3 input, un pour le titre du problème, un selecteur afin d'en choisir la branche et un autre pour le décrire et un bouton pour l'instant qui envoie les informations dans le stockage local.

Analysons le code qui permet de l'envoyer dans le stockage local.

```{figure} figures/Code_localStorage.png
---
width: 100%
---
Exemple du CommentLayer 
```
Tout d'abord, nous prenons toutes les publications. Puis nous trouvons l'id le plus grand et ajoutons 1. L'id sert d'identificateur pour supprimer une annonce, il faut alors qu'il soit unique, en cas d'erreur deux publications pourraient être supprimées.

Ensuite, nous créons un object, qui contient toutes les informations sur le créateur et les nouvelles variables nécessaires pour le componsant PostLayer, que nous le mettons dans l'array d'annonces.

Finalement, nous enregistrons l'array dans le stockage local et remettons les variables de texte à 0.


## Explication des fichiers

Je voudrais vous présenter les fichiers de mon projet

### 




