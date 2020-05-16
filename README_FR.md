# Auto-complétion en Python
API de auto-complétion basé sur des arbres trie, ecrit en utilisant la bibliothèque standard de Python. Mis à 
disposition via API web, qui renvoie un objet JSON.

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

- Une façon d'améliorer la pertinence des suggestions est de permettre des erreurs d'orthographe mineures, en 
  permettant au Trie de rechercher non seulement le chemin exact mais également les chemins à proximité avec des 
  nœuds proches de l'orthographe correcte, ce qui lui permettra de reconnaître les mots légèrement mal orthographiés.
  
  Nous pourrions également ajouter un score de priorité à certains mots qui sont peut-être plus courants / importants 
  en stockant le score dans le nœud feuille de chaque mot et en présentant le résultat en fonction du score de priorité.
  Ce score pourrait également être basé sur la fréquence des recherches effectuées par l'utilisateur, en conservant un 
  compteur de recherches dans le nœud feuille de chaque mot.
  
  Plus d'options que j'ai trouvées au cours de mes recherches peuvent être trouvées ici 
  (https://stackoverflow.com/questions/2901831/algorithm-for-autocomplete)

Q) Comment gérer un dictionnaire de termes de taille plus conséquente?

- Après ma première tentative de force brute inefficace, j'ai réalisé qu'il y avait en fait une structure de données 
  qui est particulièrement optimale pour l'auto-complétion. Ceci est la structure de données de l'arbre Trie
  (https://en.wikipedia.org/wiki/Trie), qui est rapide pour insérer et récupérer des chaînes, en particulier basé sur 
  la chaîne préfixes (comme c'est le cas en auto-complétion).
  
  Après un peu de recherche, j'ai découvert que l'arbre de recherche binaire dont j'avais parlé précédemment, bien 
  qu'une meilleure approche qu'une recherche par force brute de la liste, ne soit toujours pas aussi optimal qu'un 
  Trie, car la recherche binaire a un temps de recherche complexité de O (log N) où N est le nombre de termes du 
  dictionnaire.
  
  J'ai appris que l'un des avantages de l'utilisation d'un Trie est que le temps de recherche est indépendant de la 
  taille du dictionnaire de mots et que le nombre d'étapes nécessaires pour trouver un préfixe est le même que le 
  nombre de lettres du préfixe.
  
  Si nous voulions améliorer encore la mise en œuvre de l'arbre Trie, nous pourrions prendre en compte les mots avec
  les mêmes suffixes et minimiser le nombre de nœuds dans l'arbre Trie. Selon des sources en ligne, cela peut
  être fait en utilisant un Deterministic Finite Automata (https://en.wikipedia.org/wiki/Deterministic_finite_automaton),
  qui pointerait les nœuds vers des nœuds existants qui ont le même suffixe, ce qui réduit la mémoire
  utilisé par l'arbre Trie, qui est l'un des inconvénients de l'utilisation d'un arbre Trie.
  C'est apparemment une solution complexe, car un nœud feuille peut être atteint par plusieurs chemins, donc 
  l'importance d'un mot peut être associée à son chemin plutôt qu'à son nœud feuille 
  (https://futurice.com/blog/data-structures-for- saisie semi-automatique).
  
  Enfin, si nous étions contraints par la mémoire, nous pourrions implémenter un arbre de recherche ternaire 
  (https://www.geeksforgeeks.org/ternary-search-tree/), ce qui évite d'avoir potentiellement un dict de 26 lettres sous 
  chaque nœud (un pour chaque lettre de l'alphabet) comme nous le faisons dans un arbre Trie. Cela aurait alors une 
  complexité temporelle de recherche de O (h) où h est la hauteur de l'arbre.

## Notes

- Étant donné que je n'ai besoin que de créer un point d'entrée API unique sans aucune authentification et hébergé 
  localement, je devrais pouvoir utiliser le module de base `http.server` de Python. Cependant, une API de production 
  plus robuste aurait probablement besoin d'utiliser un cadre Web tel que Django ou Flask pour gérer 
  l'authentification, les cookies, les sessions, etc.
