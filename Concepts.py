

class Concepts:
    def __init__(self, description, id, level, isTerminal, known, unknown):
        self.description = description
        self.id = id
        self.level = level
        self.terminal = isTerminal
        self.val_known = known
        self.val_unknown = unknown
        self.parents = []
        self.children = []
        
    def addChild(self, node):
        self.children.append(node)
        node.parents.append(self)
        
    def addParent(self, node):
        self.parents.append(node)
        node.children.append(self)