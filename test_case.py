import re
from urllib import request
from data_structures import Trie

if __name__ == '__main__':
    """ Testing with larger lists of words """
    url_list = ["http://www.gutenberg.org/files/2554/2554-0.txt", "http://www.gutenberg.org/files/9296/9296.txt",
                "http://www.gutenberg.org/files/9798/9798.txt", "http://www.gutenberg.org/files/10799/10799.txt"]
    result_string = ""
    for url in url_list:
        response = request.urlopen(url)
        raw = response.read().decode('utf8')
        result_string = result_string + raw
    result_string = re.sub("[^a-zA-Z]+", " ", result_string)
    result_string = result_string.lower()
    result_string = result_string.split(sep=' ')
    del (result_string[0])
    print("*** Downloading done ***")
    my_trie = Trie()  # instantiate Trie structure
    for w in result_string:
        my_trie.insert(w.lower())
    print("*** Inserting done ***")
    result = my_trie.prefix_search('the')
    print(result)
    print("*** Searching done ***")
