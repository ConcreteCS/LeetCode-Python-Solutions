# Time: O(N)
# Space: O(N)
# 
# A trie (pronounced as "try") or prefix tree is a tree data structure used to 
# efficiently store and retrieve keys in a dataset of strings. There are various 
# applications of this data structure, such as autocomplete and spellchecker.
#
# Implement the Trie class:
#
# - Trie() Initializes the trie object.
# - void insert(String word) Inserts the string word into the trie.
# - boolean search(String word) Returns true if the string word is in the trie (i.e., 
# was inserted before), and false otherwise.
# - boolean startsWith(String prefix) Returns true if there is a previously inserted 
# string word that has the prefix prefix, and false otherwise.
# 
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True

from collections import defaultdict

class Node:
    def __init__(self):
        self.child = defaultdict(Node)
        self.end = False

class Trie:
    def __init__(self):
#        self.trie = {}
        self.root = Node()
        
    def insert(self, word):
#        t = self.trie
#        for w in word:
#            if w not in t:
#                t[w] = {}
#            t = t[w]
#        t['#'] = '#'
        
        cur = self.root
        for c in word:
            cur = cur.child[c]
        cur.end = True
        
    def _generalSearch(self, word):
        cur = self.root
        for c in word:
            cur = cur.child.get(c)
            if cur is None:
                return [False]
        return [True, cur.end]

    def search(self, word):
#        t = self.trie
#        for w in word:
#            if w not in t:
#                return False
#            t = t[w]
#        if '#' in t:
#            return True
#        return False
    
        return all(self._generalSearch(word)) 

    def startsWith(self, prefix):
#        t = self.trie
#        for w in prefix:
#            if w not in t:
#                return False
#            t = t[w]
#        return True
    
        return any(self._generalSearch(prefix))
        
# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
obj.insert("applic")
#print(obj)
print(obj.search("apple"))
print(obj.search("appled"))
print(obj.startsWith("app"))