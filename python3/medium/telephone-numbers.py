class Node():    
    def __init__(self, char):
        self.char = char
        self.children = []

    def add(self, word):
        node = self
        for char in word:
            found = False
            for child in node.children:
                if child.char == char:
                    node = child
                    found = True
                    break
            if not found:
                new_node = Node(char)
                node.children.append(new_node)
                node = new_node
    
    def count(self):
        counter = len(self.children)
        for child in self.children:
            counter += child.count()
        return counter

t = Node("")
for i in range(int(input())):
    t.add(input())
print(t.count())
