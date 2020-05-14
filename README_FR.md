# Auto-complétion en Python

Outil de auto-complétion ecrit en utilisant seulement la bibliothèque standard de Python. Mis à disposition via 
API web, qui renvoie un objet JSON.

## Exigences (sp?)
- Python 3

## Tester
`python webserver.py`
## Contraintes
Système implémenté uniquement avec la bibliothèque standard de Python. Docs à https://docs.python.org/3/library/.

## Améliorations 

- Since I only need to create a single API endpoint without any authentication hosted locally, I can get away with
  using Python's `http.server` module. However, a more robust production API would likely
  need to use a web framework such as Django or Flask to handle authentication, cookies, sessions etc.
- The format in which the data is stored depends largely on the volume. Currently because the data is so small, and
  given its one dimensional nature, a dynamic array (python list) should work well
  as it has constant (O(1)) time complexity for look ups.
- However I believe my solution has O(N) time complexity where N is the number of elements of the
  dictionary of terms as it iterates over all elements. Maybe rather than iterating over all elements I could improve
  it to just iterate until the first 4 matches are done, but then it will still at some times need to look at all 
  elements, e.g. if the 4th match is the last element in the list. 
- Out of curiosity I looked up the maximum number of elements a python list can store and it appears
  to be approx. 536,870,912 elements (on a 32 bit system), so as long as our list of dictionary values remains below 
  that we should be fine.
- Adding the ability to specify your own dictionary of terms would a good next step
- It would be nice to do some filtering of the dictionary before searching it, especially if it's already sorted,
  because there's no point searching the whole thing if we're only interested in words starting with the first letter
  of the query word.
- Checking if the dictionary is sorted in autocomplete.py may be redundant if it is iterating over every item.
- Maybe Binary Search would be a better way of searching for the matches since it's a sorted list?  
- But then if I wanted to use something like `bisect` to do a binary search, I'd need the data structure to have a
  hashed key, which would mean iterating over the whole strucutre to add the key anyway, which seems equivalent
  in performance to my current solution.
- Definitely would need to add some input checking because atm if we pass in nothing it matches everything