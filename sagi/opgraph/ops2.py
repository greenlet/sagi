

from enum import Enum



NodeToken = Enum('NodeToken', [
    'Type',
    'Var',
    'Func',
])

EdgeToken = Enum('EdgeToken', [
    'Is',
    'Val',
    'Ref',
])

class Node:
    token: NodeToken

    def __init__(self, token: NodeToken):
        self.token = token
        self.x = 1
        # print('Node self dir: ', dir(self))
        # print('Node self dict: ', self.__dict__)
        # print('Node class dir: ', dir(Node))
        # print('Node class dict: ', Node.__dict__)
        print(isinstance(self.__dict__['token'], NodeToken))


class Edge:
    n1: Node
    n2: Node
    token: EdgeToken

    def __init__(self, n1: Node, n2: Node, token: EdgeToken):
        self.n1 = n1
        self.n2 = n2
        self.token = token




def test_enum():
    for node_token in NodeToken:
        print(f'NodeToken: {node_token}. Value: {node_token.value}')

    for edge_token in EdgeToken:
        print(f'EdgeToken: {edge_token}. Value: {edge_token.value}')


def test_node():
    node = Node(NodeToken.Type)
    print('Created node: ', node)
    print('Node token: ', node.token)
    print('Node x: ', node.x)


if __name__ == '__main__':
    # test_enum()
    test_node()
