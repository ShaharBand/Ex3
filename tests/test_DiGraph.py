import random
import unittest
from DiGraph import DiGraph


def random_graph_creator(amount_of_nodes=10) -> (DiGraph, int):
    """
    This function is responsible to return a new graph with a given amount of nodes and the amount of edges in it.
    the graph will have random edges equal or less to the amount of nodes with weight values between 0 - 10.
    @:param amount_of_nodes - the amount of nodes in the graph.
    @:return a tuple containing the graph and the amount of edges in it.
    """
    g = DiGraph()

    for i in range(amount_of_nodes):
        g.add_node(i)

    edge_count = 0
    for i in range(amount_of_nodes):
        success = g.add_edge(random.randrange(0, amount_of_nodes), random.randrange(0, amount_of_nodes),
                             random.randrange(0, 10))
        if success is True:
            edge_count += 1

    return g, edge_count


class TestDiGraph(unittest.TestCase):

    def test_v_size(self):
        v_size = random.randrange(10, 20)

        g = random_graph_creator(v_size)[0]
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

    def test_e_size(self):
        v_size = random.randrange(10, 20)

        graph_creator = random_graph_creator(v_size)
        g = graph_creator[0]
        e_size = graph_creator[1]

        self.assertEqual(e_size, g.e_size(), "Failed (DiGraph: e_size()), incorrect amount of edges.")

        g.add_node(21)
        self.assertEqual(e_size, g.e_size(), "Failed (DiGraph: e_size()), incorrect amount of edges."
                                             " (after adding a new node).")

        g.add_edge(0, 21, 5)
        e_size += 1
        self.assertEqual(e_size, g.e_size(), "Failed (DiGraph: e_size()), incorrect amount of edges."
                                             " (after adding a new edge).")

        g.add_edge(0, 21, 5)
        self.assertEqual(e_size, g.e_size(), "Failed (DiGraph: e_size()), incorrect amount of edges."
                                             " (after adding an already existing edge).")

        g.add_edge(0, 22, 5)
        self.assertEqual(e_size, g.e_size(), "Failed (DiGraph: e_size()), incorrect amount of edges."
                                             " (after adding unavailable edge).")

        g.add_edge(23, 22, 5)
        self.assertEqual(e_size, g.e_size(), "Failed (DiGraph: e_size()), incorrect amount of edges."
                                             " (after adding unavailable edge).")

        g.add_edge(0, 0, 5)
        self.assertEqual(e_size, g.e_size(), "Failed (DiGraph: e_size()), incorrect amount of edges."
                                             " (after adding node edge to himself -> unavailable).")

        g.remove_edge(0, 21)
        e_size -= 1
        self.assertEqual(e_size, g.e_size(), "Failed (DiGraph: e_size()), incorrect amount of edges."
                                             " (after removing an edge).")

        g.add_edge(0, 21, -5)
        self.assertEqual(e_size, g.e_size(), "Failed (DiGraph: e_size()), incorrect amount of edges."
                                             " (after adding negative weight edge.")

    def test_get_all_v(self):
        v_size = random.randrange(10, 20)
        g = random_graph_creator(v_size)[0]

        self.assertEqual(len(g.get_all_v()), v_size,
                         "Failed (DiGraph: get_all_v()), incorrect amount of elements in the "
                         "dictionary.")

        for i in g.get_all_v():
            self.assertEqual(g.get_node(i), g.get_all_v()[i], "Failed (DiGraph: get_all_v()), incorrect elements in the"
                                                              "dictionary.")

    def test_get_mc(self):
        v_size = random.randrange(10, 20)

        graph_creator = random_graph_creator(v_size)
        g = graph_creator[0]
        e_size = graph_creator[1]
        self.assertEqual(e_size + v_size, g.get_mc(), "Failed (DiGraph: get_mc()), incorrect amount of mc.")

        g.add_node(0)
        self.assertEqual(e_size + v_size, g.get_mc(), "Failed (DiGraph: get_mc()), incorrect amount of mc"
                                                      " (after adding an already existing node).")

        g.add_node(21)
        self.assertEqual(e_size + v_size + 1, g.get_mc(), "Failed (DiGraph: get_mc()), incorrect amount of mc"
                                                          " (after adding new node).")

        g.add_edge(21, 0, 5)
        self.assertEqual(e_size + v_size + 2, g.get_mc(), "Failed (DiGraph: get_mc()), incorrect amount of mc"
                                                          " (after adding new edge).")

        g.add_edge(21, 0, 5)
        self.assertEqual(e_size + v_size + 2, g.get_mc(), "Failed (DiGraph: get_mc()), incorrect amount of mc"
                                                          " (after adding an already existing edge).")

        g.remove_edge(21, 0)
        self.assertEqual(e_size + v_size + 3, g.get_mc(), "Failed (DiGraph: get_mc()), incorrect amount of mc"
                                                          " (after removing edge).")

        g.remove_edge(21, 0)
        self.assertEqual(e_size + v_size + 3, g.get_mc(), "Failed (DiGraph: get_mc()), incorrect amount of mc"
                                                          " (after removing non-existing edge).")

        g.remove_edge(0, 0)
        self.assertEqual(e_size + v_size + 3, g.get_mc(), "Failed (DiGraph: get_mc()), incorrect amount of mc"
                                                          " (after removing connecting edge to himself).")

        g.remove_node(21)
        self.assertEqual(e_size + v_size + 4, g.get_mc(), "Failed (DiGraph: get_mc()), incorrect amount of mc"
                                                          " (after removing node).")

        g.remove_node(21)
        self.assertEqual(e_size + v_size + 4, g.get_mc(), "Failed (DiGraph: get_mc()), incorrect amount of mc"
                                                          " (after removing non-existing node).")

    def test_add_node(self):
        v_size = random.randrange(10, 20)

        graph_creator = random_graph_creator(v_size)
        g = graph_creator[0]

        self.assertTrue(g.add_node(21), "Failed (DiGraph: add_node()), failed to add a new node.")
        self.assertFalse(g.add_node(21), "Failed (DiGraph: add_node()), failed to add a new node. "
                                         "(after adding an already existing node)")

    def test_add_edge(self):
        v_size = random.randrange(10, 20)

        graph_creator = random_graph_creator(v_size)
        g = graph_creator[0]

        self.assertTrue(g.add_edge(0, 1, 5), "Failed (DiGraph: add_edge()), failed to add a new edge.")
        self.assertFalse(g.add_edge(0, 1, 5), "Failed (DiGraph: add_edge()), failed to add a new edge. "
                                              "(after adding an already existing edge)")
        self.assertFalse(g.add_edge(1, 1, 5), "Failed (DiGraph: add_edge()), failed to add a new edge. "
                                              "(after adding an node to himself as edge)")

    def test_remove_node(self):
        v_size = random.randrange(10, 20)

        graph_creator = random_graph_creator(v_size)
        g = graph_creator[0]

        self.assertTrue(g.remove_node(0), "Failed (DiGraph: remove_node()), failed to remove node.")
        self.assertFalse(g.remove_node(0), "Failed (DiGraph: remove_node()), failed to remove node. "
                                           "(after removing an already removed node)")
        self.assertFalse(g.remove_node(21), "Failed (DiGraph: remove_node()), failed to remove node. "
                                            "(after removing an non-existing node)")

    def test_remove_edge(self):
        v_size = random.randrange(10, 20)

        graph_creator = random_graph_creator(v_size)
        g = graph_creator[0]

        g.add_node(21)
        g.add_edge(0, 21, 10)
        self.assertTrue(g.remove_edge(0, 21), "Failed (DiGraph: remove_edge()), failed to remove edge.")
        self.assertFalse(g.remove_edge(0, 21), "Failed (DiGraph: remove_edge()), failed to remove edge. "
                                               "(after removing an already removed edge)")

        self.assertFalse(g.remove_edge(0, 0), "Failed (DiGraph: remove_edge()), failed to remove edge. "
                                              "(after removing an non-existing edge)")
        self.assertFalse(g.remove_edge(0, 22), "Failed (DiGraph: remove_edge()), failed to remove edge. "
                                               "(after removing an non-existing edge)")
