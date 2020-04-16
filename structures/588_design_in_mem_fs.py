# Nathan Zhu April 9th, 2020 10:41 am
# Leetcode 588 | hard | kind of hard
# Category: Design
# 

import collections
Trie = lambda: collections.defaultdict(Trie)

class FileSystem(object):

    def __init__(self):
        self.fs = Trie()
        self.file_contents = collections.defaultdict(str)

    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        if path in self.file_contents: return path.split("/")[-1:]
        
        currdir = self.fs
        for item in path.split("/"):
            if item in currdir: 
                currdir = currdir[item]
            elif item: 
                return []
            
        return sorted(currdir.keys())

    def mkdir(self, path):
        """
        :type path: str
        :rtype: None
        
        """
        curr = self.fs
        for item in path.split("/"):
            if item: curr = curr[item]
            

    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: None
        """
        self.mkdir(filePath)
        self.file_contents[filePath] = self.file_contents[filePath] + content

    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        return self.file_contents[filePath]
