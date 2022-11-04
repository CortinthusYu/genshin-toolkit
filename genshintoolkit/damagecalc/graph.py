from genshintoolkit.gtcommon.gtenum import EnumStats

class Node:
    '''docstring here'''
    def __init__(self,
                    unique_name:str,
                    description:str,
                    configuration:dict,
                    calc_func:callable,
                    node_type='add'
                ):
        self.unique_name=unique_name
        self.description=description
        self.anchors_head=[]
        self.anchors_tail=[]
        self.anchors_head_solved=[]
        self.type=type
        self.configuration =  configuration
        self.calc_func = calc_func
        self.node_type = node_type
        self.value_old = None
        self.value = 0 if self.type == 'add' else 1

    def add_tail(self,destination):
        self.anchors_tail.append(destination)
        destination.anchors_head.append(self)

    def remove_tail(self,destination):
        for i,n in enumerate(self.anchors_head):
            if id(n)==id(destination):
                self.anchors_head.pop(i)
        for i,n in enumerate(destination.anchors_tail):
            if id(n) == id(self):
                self.anchors_head.pop(i)

    def get_subnodes(self):
        return self.anchors_head

    def reset(self):
        self.anchors_head_solved.clear()
        self.value = 0 if self.type == 'add' else 1

    def solve(self):
        for n in self.anchors_head:
            if self.type=='add':
                self.value += n.solve()
            elif self.type == 'multiply':
                self.value *= n.solve()
            self.anchors_head_solved.append(n)
        return self.value

    def push(self):
        for n in self.anchors_head:
            # update value
            # and push upper nodes
            if n.type == 'add':
                self.value_old = self.value
                # self.value  = self.calc_func(self,self.configuration)
                n.value -= self.value_old
                n.value += self.value
            elif n.type == 'multiply':
                self.value_old = self.value
                n.value /= self.value_old
                n.value *= self.value
            
            n.push()

    