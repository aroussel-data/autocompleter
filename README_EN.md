# Python Autocompleter
A basic autocompletion tool written using only the Python standard library. Made available via
web API, returning a JSON object.

## Requirements
Python 3.8

## Testing
From the `autocompleter/` directory

Launch the web server using: `python webserver.py`

In a browser, enter: `http://127.0.0.1:8000/autocomplete?query=crypt`

## Constraints
No use of any external python libraries, limited to the Standard Python Library whose
docs can be found at https://docs.python.org/3/library/.

## Improvements
Q) How to improve the relevance of the suggestions?

- Perhaps we could combine duplicate fields, such as 'computer network defense', 'data', or 'symmetric'
  or pre-make some categories such as cryptography. One other option might be using user's past search
  history to predict which word they're most likely to search for. 

Q) How to handle larger lists of terms?

- Out of curiosity I looked up the maximum number of elements a python list can store and it appears
  to be approx. 536,870,912 elements (on a 32 bit system), and there are only approx. 170k and 130k words in
  English and French languages respectively, so maybe we wouldn't exceed this number!
  
  But to attempt to answer the question, normally python lists (dynamic arrays) have constant O(1) time complexity for
  lookups. However, I believe this is only if we know the value or index of the value in the list. In my case, because
  we want to match the start of a string in a potentially unsorted list of strings, some amount of iteration over the
  list is required.
  
  I thought about implementing a solution like Binary Search which would use the python built in `bisect`, but then
  I realised that this would most likely require the data structure to have a index/hashed key and that creating this
  index/hashed key would require iterating over the list anyway, which seemed redundant. That is why I settled on a
  solution which iterates over the list once, and so should have a linear time complexity O(N), where N is the number
  of elements in the list. 
  One improvement might be rather than iterating over all elements we could iterate until the first 4 
  matches are done, but there is also no guarantee that the elements that will match are not at the end of the list so
  we might still need to iterate over all elements, e.g. if the 4th match is the last element in the list.
  
  I think for truly large lists we would need to consider a database rather than in-memory processing.    

## Notes

- Since I only need to create a single API endpoint without any authentication and hosted locally, I should be able to
  use Python's basic `http.server` module. However, a more robust production API would probably need to use a web 
  framework such as Django or Flask to handle authentication, cookies, sessions etc. 
- Adding the ability to specify your own dictionary of terms would a good next step  
