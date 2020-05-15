# Auto-complétion en Python

Outil de auto-complétion ecrit en utilisant seulement la bibliothèque standard de Python. Mis à disposition via 
API web, qui renvoie un objet JSON.

## Exigences
Python 3

## Tester
Téléchargez le répertoire `git clone https://github.com/aroussel-data/autocompleter.git` ou téléchargez au format .zip.

Depuis le répertoire `autocompleter/`

Lancez le serveur web: `python webserver.py`

Dans un browser, entrez: `http://127.0.0.1:8000/autocomplete?query=crypt`

## Contraintes
Système implémenté uniquement avec la bibliothèque standard de Python. Docs à https://docs.python.org/3/library/.

## Améliorations 
Q) Comment améliorer la pertinence des suggestions faites? 

- Peut-être pourrions-nous combiner des champs en double, tels que 'computer network defense', 'data' ou 
  'symmetric' ou pré-créer certaines catégories telles que la 'cryptography'. Une autre option pourrait être d'utiliser 
  l'historique de recherche de l'utilisateur pour prédire le mot qu'il est le plus susceptible de rechercher. 

Q) Comment gérer un dictionnaire de termes de taille plus conséquente?

- Par curiosité, j'ai recherché le nombre maximum d'éléments qu'une liste python peut stocker et il semble être 
  approximativement 536 870 912 elements (sur un systeme 32 bit), et il n'y a qu'environ 170 000 et 130 000 mots 
  respectivement en anglais et en français, alors peut-être que nous ne dépasserions pas ce nombre!
  
  Mais pour tenter de répondre à la question, normalement les listes pythons (tableaux dynamiques) ont une complexité
  temporelle constante O(1) pour les recherches. Par contre, je crois que ce n'est que si nous connaissons la valeur 
  ou l'indice de la valeur dans la liste. Dans mon cas, parce que nous voulons faire correspondre le début d'une chaîne 
  dans une liste de chaînes potentiellement non triées, une certaine quantité d'itération sur la liste est nécessaire.
  
  J'ai pensé à implémenter une solution comme la recherche binaire qui utiliserait le built in de python `bisect`, mais 
  j'ai réalisé que cela nécessiterait très probablement que la structure de données ait une clé d'index / de hachage et 
  que la création de cette clé d'index / de hachage nécessiterait de toute façon une itération sur la liste, ce qui 
  me semblait redondant. C'est pourquoi j'ai choisi une solution qui itère une fois sur la liste, et devrait donc avoir 
  une complexité temporelle linéaire O(N), où N est le nombre d'éléments dans la liste. 
  Une amélioration pourrait être plutôt que d'itérer sur tous les éléments que nous pourrions répéter jusqu'à ce que les
  4 premières correspondances soient terminées, mais il n'y a également aucune garantie que les éléments qui 
  correspondront ne sont pas à la fin de la liste, nous pourrions donc avoir besoin de répéter sur tous les éléments, 
  par exemple, si la 4ème correspondance est le dernier élément de la liste.
  
  Je pense que pour des listes vraiment volumineuses, nous devrions envisager une base de données plutôt qu'un 
  traitement en mémoire.    

## Notes

- Étant donné que je n'ai besoin que de créer un point d'entrée API unique sans aucune authentification et hébergé 
  localement, je devrais pouvoir utiliser le module de base `http.server` de Python. Cependant, une API de production 
  plus robuste aurait probablement besoin d'utiliser un cadre Web tel que Django ou Flask pour gérer 
  l'authentification, les cookies, les sessions, etc. 
- Ajouter la possibilité de spécifier votre propre dictionnaire de termes serait une bonne prochaine étape.