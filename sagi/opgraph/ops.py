from enum import Enum
from typing import List, Set, Tuple, Dict, Optional, Any, Union


class Edge:
    from_node: 'Node'
    to_node: 'Node'
    directed: bool

    def __init__(self, from_node: 'Node', to_node: 'Node', directed: bool):
        self.from_node = from_node
        self.to_node = to_node
        self.directed = directed


class Node:
    edges_in: List[Edge]
    edges_out: List[Edge]
    edges: List[Edge]
    parent_nodes: Set['Node']
    child_nodes: Set['Node']
    neighbors: Set['Node']
    
    def __init__(self):
        self.edges_in = []
        self.edges_out = []
        self.edges = []
        self.parent_nodes = set()
        self.child_nodes = set()
        self.neighbors = set()
    
    def add_child(self, child: 'Node'):
        if child in self.child_nodes:
            return
        edge = Edge(self, child, directed=True)
        self.edges_out.append(edge)
        self.child_nodes.add(child)
        child.add_parent(self)
    
    def add_parent(self, parent: 'Node'):
        if parent in self.parent_nodes:
            return
        edge = Edge(parent, self, directed=True)
        self.edges_in.append(edge)
        self.parent_nodes.add(parent)
        parent.add_child(self)

    def add_neighbor(self, neighbor: 'Node'):
        if neighbor in self.neighbors:
            return
        edge = Edge(self, neighbor, directed=False)
        self.edges.append(edge)
        self.neighbors.add(neighbor)
        neighbor.add_neighbor(self)


class TypeNode(Node):
    pass


class BinTypeNode(Node):
    zero: Node
    one: Node

    def __init__(self):
        super().__init__()
        self.zero = Node()
        self.one = Node()

type_node = TypeNode()
bin_type_node = BinTypeNode()


class BinVal_Op_Or(Node):
    def __init__(self):
        super().__init__()


class VarNode(Node):
    type_node: Node

    def __init__(self, type_node: Node):
        super().__init__()
        self.type_node = type_node
        self.add_neighbor(type_node)


class ListTypeNode(Node):
    pass


class ListImpNode(Node):
    type_node: ListTypeNode
    left: Optional['ListImpNode']
    right: Optional['ListImpNode']
    value: Optional[TypeNode]

    def __init__(self):
        self.type_node = ListTypeNode()
        self.add_neighbor(self.type_node)
        self.left = None
        self.right = None
        self.value = None
    

class ListNode_PushBack(Node):
    def __init__(self):
        self.add_child(VarNode(ListNode))
        create_if_the_else
    
    def apply(self, lst: ListNode, val: TypeNode):
        # Placeholder for push back logic
        pass
        


class IntVal(Node):
    _bits: List[BinVal]

    def __init__(self, val_str: Optional[str] = None, bits: Optional[List[BinVal]] = None):
        val_str_is_none, bits_is_none = val_str is None, bits is None
        assert val_str_is_none != bits_is_none, 'Either val_str or bits must be provided, but not both'
        if val_str is not None:
            self._bits = [BinVal.One if c == '1' else BinVal.Zero for c in val_str[::-1]]
        else:
            self._bits = bits
        self._bits = bits
        if len(self._bits) > 0:
            self.




class LoopN(Node):
    n: IntVal

    def __init__(self, n: IntVal):
        self.n = n

    def apply(self, body: Node, init: IntVal, cond: Node, step: Node) -> IntVal:
        # Placeholder for loop logic
        pass


class SumInt(Node):
    def __init__(self):
        pass

    def apply(self, a: IntVal, b: IntVal) -> IntVal:
        # Placeholder for addition logic
        pass


    
