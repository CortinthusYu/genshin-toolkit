from genshintoolkit.gtcommon.gtenum import *

class Node:
    ```A Node object for damage calculation ```
    def __init__(self,
                    unique_name:str,
                    description:str,
                    type='add'
                ):
        self.unique_name=unique_name
        self.description=description
        self.anchors_head=[]
        self.anchors_tail=[]
        self.anchors_head_solved=[]
        self.type=type
        self.value = 0 if self.type == 'add' else 1

    def add_tail(self,destination:Node):
        self.anchors_tail.append(destination)
        destination.anchors_head.append(self)

    def remove_tail(self,destination):
        for i,n in enumerate(self.anchors_head):
            if id(n)==id(destination):
                pop(i)
        for i,n in enumerate(destination.anchors_tail):
            if id(n) == id(self):
                pop(i)

    def get_subnodes(self):
        return anchors_head+anchors_head_solved

    def reset(self):
        self.anchors_head_solved.clear()
        self.value = 0 if self.type == 'add' else 1

    def solve(self):
        for n in anchors_head:
            if self.type=='add':
                self.value += n.solve()
            elif self.type == 'multiply':
                self.value *= n.solve()
            anchors_head_solved.append(n)
        return self.value

    def update(self):
        pass

    def push(self):
        for n in anchors_head:
            pass

    