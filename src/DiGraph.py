from EdgeData import EdgeData
from GeoLocation import GeoLocation
from GraphInterface import GraphInterface
from NodeData import Node


class DiGraph(GraphInterface):
    """
    This class is responsible for the weighted directional graph logic
    by using variety of elements (NodeData, GeoLocation, EdgeData) while implementing the GraphInterface.
    """
    def __init__(self):
        self.__nodes = {}
        self.__edges = {}
        self.__mc = 0

    def get_node(self, key: int) -> Node:
        """
        This function is responsible to return the node within a given key associated with the graph.
        @:param key - the node's key.
        @:return the node within a given key associated with the graph.
        """
        return self.__nodes.get(str(key))

    def get_all_edges(self) -> dict:
        return self.__edges

    def get_edge(self, src: int, dest: int) -> EdgeData:
        """
        This function is responsible to return the edge data within a given source and destination associated with the graph.
        @:param src - the edge's source key.
        @:param dest - the edge's destination key.
        @:return the edge data within a given source and destination associated with the graph.
        """
        if not str(src) in self.__nodes or not str(dest) in self.__nodes:
            return False
        if src == dest:
            return False
        if not str(src) + ":" + str(dest) in self.__edges:
            return False

        return self.__edges[str(src) + ":" + str(dest)]

    def get_neighbors(self, src: int) -> list:
        """
        This function is responsible to return a list of edges within a given source associated with the graph.
        @:param src - the edge's source key.
        @:return a list of edges within a given source associated with the graph.
        """
        if not str(src) in self.__nodes:
            return False

        list_of_neighbors_keys = self.get_node(src).get_neighbors()
        list_of_neighbors = []

        for i in list_of_neighbors_keys:
            list_of_neighbors.append(self.get_edge(src=src, dest=i))

        return list_of_neighbors

    def get_edges(self, key: int) -> list:
        """
        This function is responsible to return a list of all edges associated with a given key in the graph.
        @:param key - the key associated with the edges.
        @:return a list of all edges associated with a given key in the graph.
        """
        if not str(key) in self.__nodes:
            return False

        list_of_neighbors = self.get_node(key).get_neighbors()
        list_of_dest = self.get_node(key).get_dest()
        list_of_edges = []

        for i in list_of_neighbors:
            list_of_edges.append(self.get_edge(src=key, dest=i))

        for i in list_of_dest:
            list_of_edges.append(self.get_edge(src=i, dest=key))

        return list_of_edges

    def v_size(self) -> int:
        """
        This function is responsible to return the amount of nodes associated with this graph.
        @:return the amount of nodes associated with this graph.
        """
        return len(self.__nodes)

    def e_size(self) -> int:
        """
        This function is responsible to return the amount of edges associated with this graph.
        @:return the amount of edges associated with this graph.
        """
        return len(self.__edges)

    def get_mc(self) -> int:
        """
        This function is responsible to return the Mode Count - for testing changes in the graph.
        @:return the graph Mode Count.
        """
        return self.__mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.

        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """
        if not str(id1) in self.__nodes or not str(id2) in self.__nodes:
            return False
        if id1 == id2:
            return False
        if weight < 0:
            return False
        if str(id1) + ":" + str(id2) in self.__edges:
            return False

        self.get_node(id1).add_neighbor(id2)
        self.get_node(id2).add_dest(id1)

        edge = EdgeData(src= id1, dest= id2, weight= weight)
        self.__edges[str(id1) + ":" + str(id2)] = edge
        self.__mc += 1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.

        Note: if the node id already exists the node will not be added
        """
        if str(node_id) in self.__nodes:
            return False

        if pos == None:
            pos = (None,None,None)
        node = Node(key=node_id, location=GeoLocation(pos[0], pos[1], pos[2]))
        self.__nodes[str(node_id)] = node
        self.__mc += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.

        Note: if the node id does not exists the function will do nothing
        """
        if not str(node_id) in self.__nodes:
            return False

        list_of_edges = self.get_edges(node_id)
        for i in list_of_edges:
            self.remove_edge(i.get_src(), i.get_dest())

        del self.__nodes[str(node_id)]
        self.__mc += 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.

        Note: If such an edge does not exists the function will do nothing
        """
        if not str(node_id1) in self.__nodes or not str(node_id2) in self.__nodes:
            return False
        if node_id1 == node_id2:
            return False
        if not str(node_id1) + ":" + str(node_id2) in self.__edges:
            return False

        self.get_node(node_id1).remove_neighbor(node_id2)
        self.get_node(node_id2).remove_dest(node_id1)
        self.__edges.pop(str(node_id1) + ":" + str(node_id2), None)
        self.__mc += 1
        return True

    def get_all_v(self) -> dict:
        """
        This function is responsible to return a dictionary of all the nodes in the Graph.
        @:return all the nodes in the Graph

        Note: each node is represented using a pair (key, node_data)
        """
        return self.__nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        """
        return a dictionary of all the nodes connected to (into) node_id,
        each node is represented using a pair (key, weight)
        """
        list_of_dest = self.get_node(id1).get_dest()
        dict_of_in = {}

        for i in list_of_dest:
            dict_of_in[i] = self.get_edge(i, id1).get_weight()

        return dict_of_in

    def all_out_edges_of_node(self, id1: int) -> dict:
        """
        return a dictionary of all the nodes connected from node_id, each node is represented using a pair (key,
        weight)
        """
        list_of_neighbors = self.get_node(id1).get_neighbors()
        dict_of_out = {}

        for i in list_of_neighbors:
            dict_of_out[i] = self.get_edge(id1, i).get_weight()

        return dict_of_out

    def __str__(self):
        """
        This function is responsible to return the graph in a string format.
        @return the graph data in a string format.
        """

        """
        description = "Graph Information:\nAmount of nodes: %d, Amount of edges: %d, Mode Count: %d." % \
                      (self.v_size(), self.e_size(), self.get_mc())

        description += "\n\nNodes:"
        for i in self.__nodes:
            description += "\n" + str(self.__nodes[i])

        description += "\n\nEdges:"
        for i in self.__edges:
            description += "\n" + str(self.__edges[i])

        return description
        """

        return "Graph: |V|=%d , |E|=%d." % (self.v_size(), self.e_size())

    def __repr__(self):
        return str(self)