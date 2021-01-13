import copy
import json
import math
import random

import matplotlib.pyplot as plt
from collections import deque
from typing import List

from DiGraph import DiGraph
from GeoLocation import GeoLocation
from GraphAlgoInterface import GraphAlgoInterface
from NodeData import Node
from PriorityQueue import PriorityQueue


class GraphAlgo(GraphAlgoInterface):
    """
    This class is responsible for implementing algorithms associated with weighted directional graph.
    by using variety of elements associated with DiGraph while implementing the GraphAlgoInterface.
    """

    def __init__(self, graph: DiGraph = None):
        self.__graph = graph

    def get_graph(self) -> DiGraph:
        """
        This function is responsible for returning the associated graph.
        @:return the directed graph on which the algorithm works on.
        """
        return self.__graph

    def load_from_json(self, file_name: str) -> bool:
        """
        This function is responsible to load a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
        try:
            self.__graph = DiGraph()

            file = open(file_name)
            graph_file = json.load(file)

            nodes = graph_file.get('Nodes')
            edges = graph_file.get('Edges')

            for i in nodes:
                id = i.get('id')

                if i.get('pos') is not None:
                    position = str(i.get('pos')).split(",")
                    self.__graph.add_node(node_id=int(id),
                                          pos=(float(position[0]), float(position[1]), float(position[2])))
                else:
                    self.__graph.add_node(node_id=int(id))

            for i in edges:
                src = i.get('src')
                dest = i.get('dest')
                w = i.get('w')

                self.__graph.add_edge(src, dest, w)

            file.close()

        except FileExistsError:
            return False

        return True

    def save_to_json(self, file_name: str) -> bool:
        """
        This function is responsible to save the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
        """
        if self.__graph is None:
            return False

        nodes = []
        for i in self.get_graph().get_all_v():
            id = i
            pos = self.get_graph().get_node(i).get_location()

            if pos.get_x() is not None:
                pos_str = str(pos.get_x()) + ',' + str(pos.get_y()) + "," + str(pos.get_z())
                nodes.append({"pos": pos_str, "id": id})

            nodes.append({"id": id})

        edges = []
        for i in self.get_graph().get_all_v():
            for j in self.get_graph().get_neighbors(i):
                edges.append({"src": int(j.get_src()), "dest": int(j.get_dest()), "w": float(j.get_weight())})

        graph_data = {"Edges": edges, "Nodes": nodes}

        with open(file_name, 'w') as json_file:
            json.dump(graph_data, json_file)

        return True

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, the path as a list
        """
        if self.__graph is None:
            return math.inf, None
        if str(id1) not in self.get_graph().get_all_v() or str(id2) not in self.get_graph().get_all_v():
            return math.inf, None
        if id1 == id2:
            return 0, [id1]

        self.reset_graph(-1)
        priority_queue = PriorityQueue()

        self.get_graph().get_node(id1).set_tag(0)
        priority_queue.push(self.get_graph().get_node(id1))

        parent_dict = {str(id1): id1}

        while not priority_queue.is_empty():
            current_node = priority_queue.pop()

            if current_node.get_key() == id2:  # using the parent dictonary to make a path list
                path_list = []
                index = id2
                while index != parent_dict[str(index)]:
                    path_list.append(self.get_graph().get_node(index))
                    index = parent_dict[str(index)]

                path_list.append(self.get_graph().get_node(index))
                path_list.reverse()
                return current_node.get_tag(), path_list

            for i in self.get_graph().get_neighbors(current_node.get_key()):
                neighbor_id = i.get_dest()
                neighbor = self.get_graph().get_node(neighbor_id)

                if neighbor.get_tag() == -1:
                    neighbor.set_tag(i.get_weight() + current_node.get_tag())
                    priority_queue.push(neighbor)

                    parent_dict[str(neighbor.get_key())] = current_node.get_key()

                elif priority_queue.get_key(neighbor) > i.get_weight() + current_node.get_tag():
                    priority_queue.remove(neighbor)

                    neighbor.set_tag(i.get_weight() + current_node.get_tag())
                    priority_queue.push(neighbor)
                    parent_dict[str(neighbor.get_key())] = current_node.get_key()

        return math.inf, None

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        @param id1: The node id
        @return: The list of nodes in the SCC

        Note: by using BFS algorithm and then reversing the graph edges
        We find strong connected components with a DFS algorithm.
        """
        list_of_bfs = self.breadth_first_search(id1)
        list_of_reversed_bfs = self.reversed_breadth_first_search(id1)

        strong_connection_list = []
        for i in list_of_bfs:
            if i in list_of_reversed_bfs and i not in strong_connection_list:
                strong_connection_list.append(i)

        strong_connection_list.sort()
        return strong_connection_list

    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC
        """
        if self.__graph is None:
            return []
        list_of_components = []

        for i in self.get_graph().get_all_v():
            allowed = True
            for j in list_of_components:
                if int(i) in j:
                    allowed = False

            if allowed:
                list_of_components.append(self.connected_component(id1= int(i)))

        return list_of_components

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
        if self.get_graph() is None:
            return

        x_values = []
        y_values = []

        for i in self.get_graph().get_all_v():
            node = self.get_graph().get_node(i)

            if node.get_location().get_x() is None or node.get_location().get_y() is None:
                node.set_location(GeoLocation(random.uniform(0, 100), random.uniform(0, 100)))

            position = [node.get_location().get_x(), node.get_location().get_y()]

            x_values.append(position[0])
            y_values.append(position[1])
            plt.text(position[0], position[1], node.get_key(), color='green')

        plt.plot(x_values, y_values, '.', color='red')

        for i in self.get_graph().get_all_v():
            node = self.get_graph().get_node(i)
            src_position = [node.get_location().get_x(), node.get_location().get_y()]

            for j in self.get_graph().get_neighbors(i):
                dest = self.get_graph().get_node(j.get_dest())
                dest_position = [dest.get_location().get_x(), dest.get_location().get_y()]

                delta_x = float(dest_position[0]) - float(src_position[0])
                delta_y = float(dest_position[1]) - float(src_position[1])
                distance = (delta_x ** 2 + delta_y ** 2) ** 0.5

                plt.arrow(src_position[0], src_position[1], delta_x, delta_y, width=0.01 * distance, color ='black')

        plt.title(self.get_graph())
        plt.show()

    def breadth_first_search(self, root: int) -> list:
        """
        This function is responsible to return a list of all the nodes connected to a given key of a node.
        @:param root - the root node to start from the BFS.
        @:return a list of all the nodes connected to a given key of a node.
        """
        if self.__graph is None:
            return []
        if str(root) not in self.get_graph().get_all_v():
            return []

        self.reset_graph()
        bfs_list = []
        bfs_queue = deque([root])

        while len(bfs_queue) > 0:
            current_node = bfs_queue.pop()

            for i in self.get_graph().get_neighbors(current_node):
                neighbor = i.get_dest()

                if self.get_graph().get_node(neighbor).get_tag() == 0:
                    bfs_queue.append(neighbor)
                    self.get_graph().get_node(neighbor).set_tag(1)

            bfs_list.append(current_node)

        return bfs_list

    def reversed_breadth_first_search(self, root: int) -> list:
        """
        This function is responsible to return a list of all the nodes connected to a given key of a node.
        in a reversed graph in which edges are reversed in direction.
        @:param root - the root node to start from the BFS.
        @:return a list of all the nodes connected to a given key of a node.
        """
        if self.__graph is None:
            return []
        if str(root) not in self.get_graph().get_all_v():
            return []

        graph_placeholder = copy.deepcopy(self.__graph)

        for i in self.get_graph().get_all_edges():
            edge_data = i.split(":")
            src = int(edge_data[0])
            dest = int(edge_data[1])
            w = graph_placeholder.get_edge(src=src, dest=dest).get_weight()

            if not self.get_graph().get_edge(dest, src):
                graph_placeholder.add_edge(id1=dest, id2=src, weight=w)
                graph_placeholder.remove_edge(node_id1=src, node_id2=dest)

        graph_placeholder_2 = copy.deepcopy(self.get_graph())

        self.__graph = graph_placeholder
        bfs_list = self.breadth_first_search(root)

        self.__graph = graph_placeholder_2
        return bfs_list

    def reset_graph(self, tag_value: int = 0):
        """
        This function is responsible to reset all nodes temporal data (aka color: e,g, white, gray, black / 0, 1, 2),
        which can be used be algorithms.
        @:param tag_value - the value in which the entire graph will be reset to.
        """
        if self.__graph is None:
            return False

        for i in self.get_graph().get_all_v():
            self.get_graph().get_node(i).set_tag(tag_value)
