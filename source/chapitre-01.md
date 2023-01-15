# Fonctionnement du projet

## Explication des composants utilisés

Comme dit précédemment, Vue.js utilise une architecture basée sur les composants. Il est donc utile d'utiliser cette fonctionnalité dès que possible pour éviter les répétitions et des codes trop longs.
### Composants de mise en page des publications
Les composants de mise en page définit la structure et la disposition des informations données. Un des avantages de cette fonctionnalité est de pouvoir l'utiliser dans l'ensemble de l'application et ainsi maintenir une forme de cohérence et d'unité.
#### PostLayer

Ce composant fut le premier crée, il permet gräce à une array d'objets de faire une publication. L'array contient le titre de la publication, la date, le nom de profil du créateur, la description du problème, la branche associée au problème, la photo de profil du créateur, le id de la publication qui permet de l'identifier et les commentaire sous forme de array. Vous pouvez voir un exemple de ce composant ci-dessous.

```{figure} figures/Exemple_Postlayer.png
---
width: 100%
---
Exemple du Postlayer 
```

Pour la partie supérieur du composant, la photo de profil et le nom de profil sont des objects cliquables qui permettent d'envoyer l'utilisateur dans la page de publication du créateur. Un bouton déroulable est aussi disponible afin de pouvoir supprimer les publications.

Ensuite, en-bas, la branche de la publication est aussi cliquable et permet de nous diriger vers la page de celle-ci. 
Puis, comme vous pouvez le voir, le titre, la description et la date sont affichés. 

Finalement, nous avons un bouton commentaire qui ouvre la section des commentaire. Nous pouvons ainsi ajouter un commentaire à l'array. Les commentaires des autres utilisateurs sont également affichés et peuvent même être commentés. 

#### CommentLayer

Ce composant fonctionne commme le PostLayer sauf que je trouvais que les commentaires n'avaient pas besoin d'autant d'informations que le PostLayer. En effet, l'array ne contient pas de titre, de branche. Vous pouvez voir un exemple de ce composant ci-dessous.

```{figure} figures/Exemple_CommentLayer.png
---
width: 100%
---
Exemple du CommentLayer 
```

Ce composant est récursif. Un composant récursif en Vue.js est un composant qui appelle lui-même de manière répétée. Cela peut être utile pour afficher des données hiérarchiques, telles que ,ici, les commentaires des commentaires par exemple. Vous pouvez voir ici un c

```{figure} figures/Diagramme_recursive.png
---
width: 100%
---
Exemple du CommentLayer 
```

### Composant pour créer une publication



## Organisation des fichiers

### 




