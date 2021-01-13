import time

from GraphAlgo import GraphAlgo

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
    print("connected_component(node_id): %f seconds" % (float(time.time() - start_time)/10))

    start_time = time.time()
    for i in range(10):
        for j in range(10):
            g.shortest_path(int(i),int(j))

    print("shortest_path(id1, id2): %f seconds" % (float(time.time() - start_time)/100))

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
    print("connected_component(node_id): %f seconds" % (float(time.time() - start_time)/10))

    start_time = time.time()
    for i in range(10):
        for j in range(10):
            g.shortest_path(int(i),int(j))

    print("shortest_path(id1, id2): %f seconds" % (float(time.time() - start_time)/100))

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
    print("connected_component(node_id): %f seconds" % (float(time.time() - start_time)/10))

    start_time = time.time()
    for i in range(3):
        for j in range(3):
            g.shortest_path(int(i),int(j))

    print("shortest_path(id1, id2): %f seconds" % (float(time.time() - start_time)/9))

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
    print("connected_component(node_id): %f seconds" % (float(time.time() - start_time)/10))

    start_time = time.time()
    for i in range(3):
        for j in range(3):
            g.shortest_path(int(i),int(j))

    print("shortest_path(id1, id2): %f seconds" % (float(time.time() - start_time)/9))

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
    print("connected_component(node_id): %f seconds" % (float(time.time() - start_time)/10))

    start_time = time.time()
    for i in range(3):
        for j in range(3):
            g.shortest_path(int(i),int(j))

    print("shortest_path(id1, id2): %f seconds" % (float(time.time() - start_time)/9))

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
    print("connected_component(node_id): %f seconds" % (float(time.time() - start_time)/10))

    start_time = time.time()
    for i in range(3):
        for j in range(3):
            g.shortest_path(int(i),int(j))

    print("shortest_path(id1, id2): %f seconds" % (float(time.time() - start_time)/9))

if __name__ == '__main__':
    check1()
    check2()
    check3()
    check4()
    check5()
    check6()
