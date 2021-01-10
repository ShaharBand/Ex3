import math
import random
import unittest
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


def random_graph_creator(amount_of_nodes=10) -> (DiGraph, int):
    """
    This function is responsible to return a new graph with a given amount of nodes and the amount of edges in it.
    the graph will have random edges equal or less to the amount of nodes with weight values between 0 - 10.
    @:param amount_of_nodes - the amount of nodes in the graph.
    @:return a tuple containing the graph and the amount of edges in it.

    Note: there is a 50% chance to give a location to a node in order to mix it up for better testing.
    """
    g = DiGraph()

    for i in range(amount_of_nodes):
        chance_location = random.randrange(0, 10)
        if chance_location > 5:
            g.add_node(node_id=i, pos=(random.randrange(0, 10), random.randrange(0, 10), random.randrange(0, 10)))

        else:
            g.add_node(i)

    edge_count = 0
    for i in range(amount_of_nodes):
        success = g.add_edge(random.randrange(0, amount_of_nodes), random.randrange(0, amount_of_nodes),
                             random.randrange(0, 10))
        if success is True:
            edge_count += 1

    return g, edge_count


class TestGraphAlgo(unittest.TestCase):
    """
    This class is responsible to test the functions in the GraphAlgo class
    """

    def test_save_load_from_json(self):
        ga = GraphAlgo()
        self.assertFalse(ga.save_to_json("testGraph.json"), "Failed (GraphAlgo: save_to_json()), failed to save "
                                                            "graph. (empty graph)")

        v_size = random.randrange(10, 20)
        g = random_graph_creator(v_size)[0]

        ga = GraphAlgo(g)

        self.assertTrue(ga.save_to_json("testGraph.json"), "Failed (GraphAlgo: save_to_json()), failed to save graph.")
        self.assertTrue(ga.load_from_json("testGraph.json"), "Failed (GraphAlgo: load_from_json()), failed to load "
                                                             "graph.")

        self.assertEqual(g.get_all_v().keys(), ga.get_graph().get_all_v().keys(),
                         "Failed (GraphAlgo: load_from_json()), failed to load graph properly. (noticed while "
                         "comparing nodes)")
        self.assertEqual(g.get_all_edges().keys(), ga.get_graph().get_all_edges().keys(),
                         "Failed (GraphAlgo: load_from_json()), failed to load graph "
                         "properly. (noticed while comparing edges)")

    def test_shortest_path(self):
        ga = GraphAlgo()
        self.assertEqual(ga.shortest_path(1, 1), (math.inf, None), "Failed (GraphAlgo: shortest_path()), failed to "
                                                                   "calculate shortest path.")

        v_size = random.randrange(10, 20)
        g = random_graph_creator(v_size)[0]
        g.add_node(21)
        g.remove_edge(0, 4)
        g.add_edge(0, 4, 1)
        g.add_edge(0, 21, 50)
        g.add_edge(4, 21, 1)
        ga = GraphAlgo(g)

        self.assertEqual(str(ga.shortest_path(0, 21)), "(2, [0, 4, 21])", "Failed (GraphAlgo: shortest_path()), "
                                                                          "failed to calculate shortest path.")

        ga.get_graph().remove_node(0)
        self.assertEqual(ga.shortest_path(0, 21), (math.inf, None), "Failed (GraphAlgo: shortest_path()), failed to "
                                                                    "calculate shortest path.")

    def test_connected_component(self):
        ga = GraphAlgo()
        self.assertEqual(ga.connected_component(0), [], "Failed (GraphAlgo: connected_component()), failed to "
                                                        "calculate connected component function.")

        v_size = random.randrange(10, 20)
        g = random_graph_creator(v_size)[0]
        g.add_node(21)
        g.add_node(22)
        g.add_node(23)

        g.add_edge(21, 22, 1)
        g.add_edge(22, 23, 1)
        g.add_edge(22, 21, 1)
        g.add_edge(23, 22, 1)
        ga = GraphAlgo(g)

        self.assertEqual(ga.connected_component(21), [21, 22, 23],
                         "Failed (GraphAlgo: connected_component()), failed to "
                         "calculate connected component function.")

        ga.get_graph().remove_edge(22, 23)
        self.assertEqual(ga.connected_component(21), [21, 22],
                         "Failed (GraphAlgo: connected_component()), failed to "
                         "calculate connected component function.")

        ga.get_graph().remove_node(21)
        self.assertEqual(ga.connected_component(21), [],
                         "Failed (GraphAlgo: connected_component()), failed to "
                         "calculate connected component function.")

        self.assertEqual(ga.connected_component(22), [22],
                         "Failed (GraphAlgo: connected_component()), failed to "
                         "calculate connected component function.")

    def test_connected_components(self):
        ga = GraphAlgo()
        self.assertEqual(ga.connected_components(), [], "Failed (GraphAlgo: connected_component()), failed to "
                                                        "calculate connected components function.")
        g = DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_edge(0, 1, 1)
        g.add_edge(0, 2, 1)
        g.add_edge(0, 3, 1)
        g.add_edge(3, 0, 1)
        g.add_edge(2, 0, 1)
        g.add_edge(1, 0, 1)
        ga = GraphAlgo(g)

        self.assertEqual(ga.connected_components(), [[0, 1, 2, 3]],
                         "Failed (GraphAlgo: connected_component()), failed to "
                         "calculate connected components function.")

        ga.get_graph().remove_node(1)
        self.assertEqual(ga.connected_components(), [[0, 2, 3]], "Failed (GraphAlgo: connected_component()), failed to "
                                                                 "calculate connected components function.")

        ga.get_graph().remove_edge(2, 0)
        self.assertEqual(ga.connected_components(), [[0, 3], [2]],
                         "Failed (GraphAlgo: connected_component()), failed to "
                         "calculate connected components function.")

    def test_plot_graph(self):
        try:
            ga = GraphAlgo()
            ga.plot_graph()

        except:
            self.fail("Failed (GraphAlgo: plot_graph()), failed to plot an empty graph.")

        try:
            v_size = random.randrange(10, 20)
            g = random_graph_creator(v_size)[0]
            ga = GraphAlgo(g)
            ga.plot_graph()

        except:
            self.fail("Failed (GraphAlgo: plot_graph()), failed to plot graph.")
