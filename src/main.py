import time

from GraphAlgo import GraphAlgo
import networkx as nx


def check1():
    print("\nCheck: V: 10 E: 80\n")
    g = GraphAlgo()
    start_time = time.time()
    g.load_from_json("../data/G_10_80_1.json")
    print("load_from_json(file_name): %f seconds" % (float(time.time() - start_time)))

    start_time = time.time()
    g.connected_components()
    print("connected_components(): %f seconds" % (float(time.time() - start_time)))

    start_time = time.time()
    for i in range(10):
        g.connected_component(int(i))
    print("connected_component(node_id): %f seconds" % (float(time.time() - start_time) / 10))

    start_time = time.time()
    for i in range(10):
        for j in range(10):
            g.shortest_path(int(i), int(j))

    print("shortest_path(id1, id2): %f seconds" % (float(time.time() - start_time) / 100))


def check2():
    print("\nCheck: V: 100 E: 800\n")
    g = GraphAlgo()
    start_time = time.time()
    g.load_from_json("../data/G_100_800_1.json")
    print("load_from_json(file_name): %f seconds" % (float(time.time() - start_time)))

    start_time = time.time()
    g.connected_components()
    print("connected_components(): %f seconds" % (float(time.time() - start_time)))

    start_time = time.time()
    for i in range(10):
        g.connected_component(int(i))
    print("connected_component(node_id): %f seconds" % (float(time.time() - start_time) / 10))

    start_time = time.time()
    for i in range(10):
        for j in range(10):
            g.shortest_path(int(i), int(j))

    print("shortest_path(id1, id2): %f seconds" % (float(time.time() - start_time) / 100))


def check3():
    print("\nCheck: V: 1000 E: 8000\n")
    g = GraphAlgo()
    start_time = time.time()
    g.load_from_json("../data/G_1000_8000_1.json")
    print("load_from_json(file_name): %f seconds" % (float(time.time() - start_time)))

    start_time = time.time()
    g.connected_components()
    print("connected_components(): %f seconds" % (float(time.time() - start_time)))

    start_time = time.time()
    for i in range(10):
        g.connected_component(int(i))
    print("connected_component(node_id): %f seconds" % (float(time.time() - start_time) / 10))

    start_time = time.time()
    for i in range(3):
        for j in range(3):
            g.shortest_path(int(i), int(j))

    print("shortest_path(id1, id2): %f seconds" % (float(time.time() - start_time) / 9))


def check4():
    print("\nCheck: V: 10k E: 80k\n")
    g = GraphAlgo()
    start_time = time.time()
    g.load_from_json("../data/G_10000_80000_1.json")
    print("load_from_json(file_name): %f seconds" % (float(time.time() - start_time)))

    start_time = time.time()
    g.connected_components()
    print("connected_components(): %f seconds" % (float(time.time() - start_time)))

    start_time = time.time()
    for i in range(10):
        g.connected_component(int(i))
    print("connected_component(node_id): %f seconds" % (float(time.time() - start_time) / 10))

    start_time = time.time()
    for i in range(3):
        for j in range(3):
            g.shortest_path(int(i), int(j))

    print("shortest_path(id1, id2): %f seconds" % (float(time.time() - start_time) / 9))


def check5():
    print("\nCheck: V: 20k E: 160k\n")
    g = GraphAlgo()
    start_time = time.time()
    g.load_from_json("../data/G_20000_160000_1.json")
    print("load_from_json(file_name): %f seconds" % (float(time.time() - start_time)))

    start_time = time.time()
    g.connected_components()
    print("connected_components(): %f seconds" % (float(time.time() - start_time)))

    start_time = time.time()
    for i in range(10):
        g.connected_component(int(i))
    print("connected_component(node_id): %f seconds" % (float(time.time() - start_time) / 10))

    start_time = time.time()
    for i in range(3):
        for j in range(3):
            g.shortest_path(int(i), int(j))

    print("shortest_path(id1, id2): %f seconds" % (float(time.time() - start_time) / 9))


def check6():
    print("\nCheck: V: 30k E: 240k\n")
    g = GraphAlgo()
    start_time = time.time()
    g.load_from_json("../data/G_30000_240000_1.json")
    print("load_from_json(file_name): %f seconds" % (float(time.time() - start_time)))

    start_time = time.time()
    g.connected_components()
    print("connected_components(): %f seconds" % (float(time.time() - start_time)))

    start_time = time.time()
    for i in range(10):
        g.connected_component(int(i))
    print("connected_component(node_id): %f seconds" % (float(time.time() - start_time) / 10))

    start_time = time.time()
    for i in range(3):
        for j in range(3):
            g.shortest_path(int(i), int(j))

    print("shortest_path(id1, id2): %f seconds" % (float(time.time() - start_time) / 9))


def check7():
    g = GraphAlgo()
    g.load_from_json("../data/G_10_80_1.json")

    G = nx.Graph()
    for i in g.get_graph().get_all_v():
        G.add_node(int(i))

    for i in g.get_graph().get_all_edges():
        src = g.get_graph().get_all_edges()[i].get_src()
        dest = g.get_graph().get_all_edges()[i].get_dest()
        weight = g.get_graph().get_all_edges()[i].get_weight()
        G.add_edge(src, dest, weight=weight)

    start_time = time.time()
    for i in range(10):
        for j in range(10):
            nx.shortest_path(G, source=int(i), target=int(j))

    print("shortest_path(id1, id2): %f seconds" % (float(time.time() - start_time) / 100))

    start_time = time.time()
    for i in range(10):
        nx.node_connected_component(G, n=i)
    print("connected_component(node_id): %f seconds" % (float(time.time() - start_time) / 10))

    start_time = time.time()
    list(nx.connected_components(G))
    print("connected_components(): %f seconds" % (float(time.time() - start_time)))


def check8():
    g = GraphAlgo()
    g.load_from_json("../data/G_100_800_1.json")

    G = nx.Graph()
    for i in g.get_graph().get_all_v():
        G.add_node(int(i))

    for i in g.get_graph().get_all_edges():
        src = g.get_graph().get_all_edges()[i].get_src()
        dest = g.get_graph().get_all_edges()[i].get_dest()
        weight = g.get_graph().get_all_edges()[i].get_weight()
        G.add_edge(src, dest, weight=weight)

    start_time = time.time()
    for i in range(10):
        for j in range(10):
            nx.shortest_path(G, source=int(i), target=int(j))

    print("shortest_path(id1, id2): %f seconds" % (float(time.time() - start_time) / 100))

    start_time = time.time()
    for i in range(10):
        nx.node_connected_component(G, n=i)
    print("connected_component(node_id): %f seconds" % (float(time.time() - start_time) / 10))

    start_time = time.time()
    list(nx.connected_components(G))
    print("connected_components(): %f seconds" % (float(time.time() - start_time)))


def check9():
    g = GraphAlgo()
    g.load_from_json("../data/G_1000_8000_1.json")

    G = nx.Graph()
    for i in g.get_graph().get_all_v():
        G.add_node(int(i))

    for i in g.get_graph().get_all_edges():
        src = g.get_graph().get_all_edges()[i].get_src()
        dest = g.get_graph().get_all_edges()[i].get_dest()
        weight = g.get_graph().get_all_edges()[i].get_weight()
        G.add_edge(src, dest, weight=weight)

    start_time = time.time()
    for i in range(10):
        for j in range(10):
            nx.shortest_path(G, source=int(i), target=int(j))

    print("shortest_path(id1, id2): %f seconds" % (float(time.time() - start_time) / 100))

    start_time = time.time()
    for i in range(10):
        nx.node_connected_component(G, n=i)
    print("connected_component(node_id): %f seconds" % (float(time.time() - start_time) / 10))

    start_time = time.time()
    list(nx.connected_components(G))
    print("connected_components(): %f seconds" % (float(time.time() - start_time)))


def check10():
    g = GraphAlgo()
    g.load_from_json("../data/G_10000_80000_1.json")

    G = nx.Graph()
    for i in g.get_graph().get_all_v():
        G.add_node(int(i))

    for i in g.get_graph().get_all_edges():
        src = g.get_graph().get_all_edges()[i].get_src()
        dest = g.get_graph().get_all_edges()[i].get_dest()
        weight = g.get_graph().get_all_edges()[i].get_weight()
        G.add_edge(src, dest, weight=weight)

    start_time = time.time()
    for i in range(10):
        for j in range(10):
            nx.shortest_path(G, source=int(i), target=int(j))

    print("shortest_path(id1, id2): %f seconds" % (float(time.time() - start_time) / 100))

    start_time = time.time()
    for i in range(10):
        nx.node_connected_component(G, n=i)
    print("connected_component(node_id): %f seconds" % (float(time.time() - start_time) / 10))

    start_time = time.time()
    list(nx.connected_components(G))
    print("connected_components(): %f seconds" % (float(time.time() - start_time)))


def check11():
    g = GraphAlgo()
    g.load_from_json("../data/G_20000_160000_1.json")

    G = nx.Graph()
    for i in g.get_graph().get_all_v():
        G.add_node(int(i))

    for i in g.get_graph().get_all_edges():
        src = g.get_graph().get_all_edges()[i].get_src()
        dest = g.get_graph().get_all_edges()[i].get_dest()
        weight = g.get_graph().get_all_edges()[i].get_weight()
        G.add_edge(src, dest, weight=weight)

    start_time = time.time()
    for i in range(10):
        for j in range(10):
            nx.shortest_path(G, source=int(i), target=int(j))

    print("shortest_path(id1, id2): %f seconds" % (float(time.time() - start_time) / 100))

    start_time = time.time()
    for i in range(10):
        nx.node_connected_component(G, n=i)
    print("connected_component(node_id): %f seconds" % (float(time.time() - start_time) / 10))

    start_time = time.time()
    list(nx.connected_components(G))
    print("connected_components(): %f seconds" % (float(time.time() - start_time)))


def check12():
    g = GraphAlgo()
    g.load_from_json("../data/G_30000_240000_1.json")

    G = nx.Graph()
    for i in g.get_graph().get_all_v():
        G.add_node(int(i))

    for i in g.get_graph().get_all_edges():
        src = g.get_graph().get_all_edges()[i].get_src()
        dest = g.get_graph().get_all_edges()[i].get_dest()
        weight = g.get_graph().get_all_edges()[i].get_weight()
        G.add_edge(src, dest, weight=weight)

    start_time = time.time()
    for i in range(10):
        for j in range(10):
            nx.shortest_path(G, source=int(i), target=int(j))

    print("shortest_path(id1, id2): %f seconds" % (float(time.time() - start_time) / 100))

    start_time = time.time()
    for i in range(10):
        nx.node_connected_component(G, n=i)
    print("connected_component(node_id): %f seconds" % (float(time.time() - start_time) / 10))

    start_time = time.time()
    list(nx.connected_components(G))
    print("connected_components(): %f seconds" % (float(time.time() - start_time)))


if __name__ == '__main__':
    check1()
    check2()
    check3()
    check4()
    check5()
    check6()

    print("networkX check:")
    check7()
    check8()
    check9()
    check10()
    check11()
    check12()
