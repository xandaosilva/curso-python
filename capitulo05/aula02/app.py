class Author:
    def __init__(self, name):
        self._name = name
        self._tool = None

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def tool(self):
        return self._tool
    
    @tool.setter
    def tool(self, tool):
        self._tool = tool


class Tool:
    def __init__(self, name):
        self._name = name

    def write(self):
        return f"{self._name} está escrevendo"

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name


author = Author("Maria")
tool = Tool("Office")
author.tool = tool

print(tool.write())
print(author.tool.write())
