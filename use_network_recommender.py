import typing as t
from network_recommender import get_most_similar_nodes, GraphNode, GraphRelationship
from network_database import GitlinkedNetworkDatabase
import enum
import pandas as pd
import networkx as nx



class NodeType(enum.Enum):
    USER = "user"
    REPOSITORY = "repository"
    TAG = "tag"



def generateGraph(db: GitlinkedNetworkDatabase) -> nx.Graph:
    # Get the relationships repositories and their top contributors

    all_user_ids = set()
    all_repository_ids = set()


    all_contributors = db.get_all_contributors()
    all_relationships: t.List[GraphRelationship] = []

    for contributor in all_contributors:
        if (type(contributor["repos"]) != dict):
            continue

        for repository_index in contributor["repos"].keys():
            user_id = str(contributor["id"])
            repository_id = contributor["repos"][repository_index]["Repository"]

            all_relationships.append(GraphRelationship(
                GraphNode(user_id, NodeType.USER.value), 
                GraphNode(repository_id, NodeType.REPOSITORY.value)
            ))
            all_user_ids.add(user_id)
            all_repository_ids.add(repository_id)


    all_user_ids = {x for x in db.get_all_user_ids()} | all_user_ids
    all_repository_ids = {x for x in db.get_all_repository_ids()} | all_repository_ids


    all_users = [GraphNode(i, NodeType.USER.value) 
            for i in all_user_ids]

    all_repositories = [GraphNode(i, NodeType.REPOSITORY.value) 
                        for i in all_repository_ids]
    
    all_tags = [GraphNode(i, NodeType.TAG.value)
                for i in db.get_all_tag_ids()]


    all_nodes = all_users + all_repositories + all_tags


    G = nx.Graph()
    for node in all_nodes:
        G.add_node(node.id)
    for relationship in all_relationships:
        G.add_edge(relationship.node1_id, relationship.node2_id)


    return G





def find_close_items(db: GitlinkedNetworkDatabase, item_id, item_type, top_n=10) -> t.Tuple[pd.DataFrame, pd.DataFrame]:

    G = generateGraph(db)

    most_similar_nodes = get_most_similar_nodes(G, item_id, item_type)


    df = pd.DataFrame([GraphNode.id_to_type_and_item_id(i[0]) + list(i)[1:] for i in most_similar_nodes],
        columns=["type", "id", "similarity"]).sort_values(by="similarity", ascending=False)

    # split the dataframe into two, based on type
    df_users = df[df["type"] == NodeType.USER.value]
    df_repositories = df[df["type"] == NodeType.REPOSITORY.value]

    # return the first n columns of each dataframe

    top_users_df = df_users.head(top_n)
    
    top_repositories_df = df_repositories.head(top_n)

