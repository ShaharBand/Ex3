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

    def test_graph_creation(self):
        v_size = random.randrange(10, 20)
        g = random_graph_creator(v_size)
        self.assertEqual(v_size, g.v_size(), "Failed! incorrect amount of nodes.")
