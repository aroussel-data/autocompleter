# Python Autocompleter
A Trie tree based autocompletion API written using the Python standard library. Made available via URL
endpoint, returning a JSON object. It returns the first 4 alphabetically sorted elements of the word
dictionary whose prefix matches the submitted query.

## Requirements
Python 3

## Testing
Clone the repo using `git clone https://github.com/aroussel-data/autocompleter.git` or download as .zip.

From the `autocompleter/` directory

Launch the web server using: `python webserver.py`

In a browser, enter: `http://127.0.0.1:8000/autocomplete?query=crypt`

## Constraints
No use of any external python libraries, limited to the Standard Python Library whose
docs can be found at https://docs.python.org/3/library/.

## Improvements
Q) How to improve the relevance of the suggestions?

- One way to improve the relevance of suggestions is to allow for minor spelling mistakes, by allowing
  for the Trie to search along not just the exact path but also nearby paths with nodes close to the
  correct spelling, which will allow it to recognise slightly misspelled words.
  
  We could also add a priority score to certain words that are perhaps more common/important by storing 
  the score in each word's leaf node, and presenting the result based on priority score. This score 
  could also be based on the frequency of times it has already been searched by the user, by keeping 
  a counter of searches in each word's leaf node.
  
  More options I came across during research can be found here 
  (https://stackoverflow.com/questions/2901831/algorithm-for-autocomplete)

Q) How to handle larger lists of terms?

- After my first inefficient brute force attempt, I realised that in fact there was a data structure that
  is particularly optimal for auto-completion. This is the Trie tree data structure 
  (https://en.wikipedia.org/wiki/Trie), which is fast at inserting and retrieving strings, especially based on string 
  prefixes (as is the case in auto-completion).
  
  After a bit of research, I found out that the Binary Search tree that I had discussed previously, while
  a better approach than a brute force search of the list, is still not as optimal as a Trie, as Binary Search
  has a search time complexity of O(log N) where N is the number of terms in the dictionary.

  I learnt that one of the advantages of using a Trie, is that the search time is independent of the size of the
  word dictionary, and that the number of steps needed to find a prefix is the same as the number of
  letters in the prefix.
  
  If we wanted to further improve the Trie tree implementation, we could take into account words with
  the same suffixes and minimise the number of nodes in the Trie tree. According to online sources this can
  be done by using a Deterministic Finite Automata (https://en.wikipedia.org/wiki/Deterministic_finite_automaton), 
  which would point nodes to existing nodes that have the same suffix, reducing the memory
  used by the Trie tree, which is one of the disadvantages of using a Trie tree.
  This is apparently a complex solution, because a leaf node can be reached through several paths, so a
  word's importance can be associated with its path rather than its leaf node
  (https://futurice.com/blog/data-structures-for-fast-autocomplete).
  
  Lastly, if we were constrained by memory, we could implement a Ternary Search Tree 
  (https://www.geeksforgeeks.org/ternary-search-tree/), which avoids having potentially a dict of 26
  letters under each node (one for each letter of the alphabet) like we do in a Trie tree. This would
  then have a search time complexity of O(h) where h is the height of the tree.
  
## Notes

- Since I only need to create a single API endpoint without any authentication and hosted locally, I should be able to
  use Python's basic `http.server` module. However, a more robust production API would probably need to use a web 
  framework such as Django or Flask to handle authentication, cookies, sessions etc.
