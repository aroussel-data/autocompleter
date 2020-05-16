class TrieNode:
    """Represents an individual node within the Trie tree structure"""
    def __init__(self):
        self.children = {}  # dict instead of list so we can look up using chars instead of creating indices
        self.word_end = False  # used to indicate a leaf node upon insertion


class Trie:
    """Represents the whole Trie tree structure"""
    def __init__(self):
        self.root = TrieNode()  # the root of our Trie tree
        self.result_list = []  # autocompleted words will go here

    def insert(self, word):
        crawler = self.root  # crawler starts at root node and moves downwards
        for char in word:
            if not crawler.children.get(char):  # if char not in children dict we add it
                crawler.children[char] = TrieNode()
            # if char in current node's children, move the crawler to that child node
            crawler = crawler.children[char]
        crawler.word_end = True  # marks the end of an inserted word aka leaf node

    def recur_match(self, final_prefix_node, word):
        if final_prefix_node.word_end and len(self.result_list) < 4:
            self.result_list.append(word)
        for letter, child_node in final_prefix_node.children.items():
            self.recur_match(child_node, word + letter)

    def prefix_search(self, prefix):
        self.result_list = []
        crawler = self.root
        for char in prefix:
            if not crawler.children.get(char):  # if current node's children don't contain char we exit
                return None
            # if char in current node's children, move the crawler to that child node
            crawler = crawler.children[char]
        # now crawler will be at node that represents end of prefix, and so should now find all the child leaves
        # that are continuations of the prefix.
        self.recur_match(crawler, prefix)
        return self.result_list


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
