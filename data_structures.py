from constants import TERMS


# a class that represents an individual node within the tree structure
class TrieNode:
    def __init__(self):
        self.children = {}  # dict instead of list so we can look up using chars instead of creating index numbers
        self.word_end = False


# a class that represents the whole tree structure
class Trie:
    # when we instantiate the Trie structure, we want it to have a root node with no children and word_end=False
    def __init__(self):
        self.root = TrieNode()
        self.result_list = []

    # method to insert an individual word from the TERMS list
    def insert(self, word):
        crawler = self.root  # every time we insert, crawler starts at root and moves downwards
        for c in word:
            if not crawler.children.get(c):
                crawler.children[c] = TrieNode()
            crawler = crawler.children[c]
        crawler.word_end = True

    def recur_match(self, leaf_node, word):
        if leaf_node.word_end and len(self.result_list) < 4:
            self.result_list.append(word)
        for letter, child_node in leaf_node.children.items():
            self.recur_match(child_node, word + letter)

    def prefix_search(self, prefix):
        crawler = self.root
        for c in prefix:
            if not crawler.children.get(c):  # if current node's children doesn't contain char we exit
                return 0
            # but if that letter's node is in node's children, move the crawler to next node
            crawler = crawler.children[c]
        self.recur_match(crawler, prefix)


if __name__ == '__main__':
    if not TERMS == sorted(TERMS):
        TERMS = sorted(TERMS)
    my_trie = Trie()
    for w in TERMS:
        my_trie.insert(w.lower())
    my_trie.prefix_search('crypt'.lower())
    print(my_trie.result_list)

    # FOR TESTING WITH LARGER LISTS (crime and punishment):
    # from urllib import request
    # import re
    #
    # url = "http://www.gutenberg.org/files/2554/2554-0.txt"
    # response = request.urlopen(url)
    # raw = response.read().decode('utf8')
    #
    # raw = re.sub("[^a-zA-Z]+", " ", raw)
    # raw = raw.lower()
    # raw = raw.split(sep=' ')
    # del (raw[0])
