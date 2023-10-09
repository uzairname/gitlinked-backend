import typing as t
from node2vec import Node2Vec
import networkx as nx
import sys, os



class GraphNode:
    def __init__(self, item_id: str, item_type: str):
        self.item_id = item_id
        self.type = item_type

        self.id = self.type + " " + self.item_id

    def id_to_type_and_item_id(id: str) -> t.List[str]:
        # returns a list of [type, id] from the id string
        return id.split(" ")


    def __repr__(self):
        return f"GraphNode({self.item_id}, {self.type})"



class GraphRelationship:
    def __init__(self, node1: GraphNode, node2: GraphNode):
        self.node1_id = node1.item_id
        self.node2_id = node2.item_id





def _train_embedding_model(graph: nx.Graph) -> Node2Vec:

    n2v = Node2Vec(graph, dimensions=32, walk_length=40, num_walks=4, workers=4)
    model = n2v.fit(window=10, min_count=1, batch_words=4)

    return model




def get_most_similar_nodes(graph: nx.Graph, item_id: str, item_type: str, topn=10):

    model = _train_embedding_model(graph)

    node_id = GraphNode(item_id, item_type).id

    return model.wv.most_similar(node_id, topn=topn)
    







