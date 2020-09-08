from typing import *

class Record(object):
    def __init__(self, record_id: int, parent_id: int):
        self.record_id: int = record_id
        self.parent_id: int = parent_id

class Node(object):
    def __init__(self, id_: int):
        self.node_id: int = id_
        self.children: List[Node] = []

def get_children_nodes(parent_node: Node, records: List[Record]):
    ids = map(lambda x: x.record_id, filter(lambda x: x.record_id and x.parent_id == parent_node.node_id, records))

    for id_ in ids:
        sub_node = Node(id_)
        parent_node.children.append(sub_node)
        get_children_nodes(sub_node, records)

def BuildTree(records: List[Record]) -> Optional[Node]:
    if not (records := sorted(records, key=lambda x: x.record_id)): return None

    for (i, r) in enumerate(records):
        if i != r.record_id: raise ValueError("Incorrect index")
        if not i and r.parent_id: raise ValueError("Error Root node")
        if i and r.record_id <= r.parent_id: raise ValueError("Incorrect parent id")

    get_children_nodes(root := Node(0), records)
    return root
