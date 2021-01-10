import random
import unittest
from DiGraph import DiGraph


def random_graph_creator(amount_of_nodes=10) -> DiGraph:
    """
    This function is responsible to return a new graph with a given amount of nodes.
    the graph will have random edges equal or less to the amount of nodes with weight values between 0 - 10.
    @:param amount_of_nodes - the amount of nodes in the graph.
    @:return a new graph.
    """
    g = DiGraph()

    for i in range(amount_of_nodes):
        g.add_node(i)

    for i in range(amount_of_nodes):
        g.add_edge(random.randrange(0, amount_of_nodes), random.randrange(0, amount_of_nodes), random.randrange(0, 10))

    print(g)
    return g


class TestDiGraph(unittest.TestCase):

    def test_v_size(self):
        v_size = random.randrange(10, 20)

        g = random_graph_creator(v_size)
        self.assertEqual(v_size, g.v_size(), "Failed (DiGraph: v_size()), incorrect amount of nodes.")

        v_size += 1
        g.add_node(21)
        self.assertEqual(v_size, g.v_size(), "Failed (DiGraph: v_size()), incorrect amount of nodes"
                                                 " (after adding a node).")

        g.add_node(21)
        self.assertEqual(v_size, g.v_size(), "Failed (DiGraph: v_size()), incorrect amount of nodes"
                                                 " (after adding an already existing node).")

        v_size -= 1
        g.remove_node(0)
        self.assertEqual(v_size, g.v_size(), "Failed (DiGraph: v_size()), incorrect amount of nodes"
                                             " (after removing a node).")

        g.remove_node(0)
        self.assertEqual(v_size, g.v_size(), "Failed (DiGraph: v_size()), incorrect amount of nodes"
                                             " (after removing a node).")

        g.add_edge(0, 1, 5)
        self.assertEqual(v_size, g.v_size(), "Failed (DiGraph: v_size()), incorrect amount of nodes"
                                             " (after adding an edge).")

        g.add_edge(0, 1, 5)
        self.assertEqual(v_size, g.v_size(), "Failed (DiGraph: v_size()), incorrect amount of nodes"
                                             " (after adding an already existing edge).")

        g.remove_edge(0, 1)
        self.assertEqual(v_size, g.v_size(), "Failed (DiGraph: v_size()), incorrect amount of nodes"
                                             " (after removing an edge).")

        g.remove_edge(0, 1)
        self.assertEqual(v_size, g.v_size(), "Failed (DiGraph: v_size()), incorrect amount of nodes"
                                             " (after removing an non existing edge).")
