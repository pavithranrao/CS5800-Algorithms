class Node:
    def __init__(self, name=None, graph_index=0):
        self.name = name
        self.graph_index = graph_index
        self.p = None
        self.next_node = None

    def __repr__(self):
        return str(self.name)


class NodesAndWeights:
    def __init__(self, v=None, w=0):
        self.v = v
        self.w = w


class Edge:
    def __init__(self, w=0, from_node=None, to_node=None):
        self.w = w
        self.from_node = from_node
        self.to_node = to_node

    def __repr__(self):
        return "{} -> {} : {}".format(self.from_node, self.to_node, self.w)

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        if (other.from_node.name == self.from_node.name) and \
                (other.to_node.name == self.to_node.name):
            return True
        if (other.from_node.name == self.to_node.name) and \
                (other.to_node.name == self.from_node.name):
            return True

    def __hash__(self):
        return hash(self.from_node) + hash(self.to_node)


class DisjointSet:
    def __init__(self, head=None):
        if head is None:
            self.head = Node("head")
            self.tail = Node("tail")
            self.head.p = self.tail
            self.tail.p = self.head
            self.head.next_node = None
            self.tail.next_node = None
        else:
            self.head = head
            self.tail = head.p

    def add(self, n):
        if self.head.next_node is None:
            self.head.next_node = n
            self.tail.next_node = n
        else:
            self.tail.next_node.next_node = n
            self.tail.next_node = n
            n.next_node = None
        n.p = self.head

    @staticmethod
    def union(a, b):
        a_head = a.p
        b_head = b.p
        t = b_head.next_node

        while t is not None:
            t.p = a_head
            t = t.next_node

        a_tail = a_head.p
        b_tail = b_head.p
        a_tail.next_node.next_node = b_head.next_node
        a_tail.next_node = b_tail.next_node

    @staticmethod
    def findSet(n):
        return n.p


class KGraph:
    def __init__(self, v=0, is_undirected=None, adj=None):
        if adj is None:
            self.adj = [[] for _ in xrange(v)]
            self.v = v
            if v != 0 and is_undirected is None:
                self.is_undirected = False

            else:
                self.is_undirected = is_undirected
        else:
            self.adj = adj
            self.is_undirected = is_undirected

    @staticmethod
    def add_edge(g, source, destination, weight):
        g.adj[source.graph_index].append(NodesAndWeights(destination, weight))
        if g.is_undirected:
            g.adj[destination.graphIndex].append(NodesAndWeights(source, weight))

    def get_vertices(self):
        return map(lambda idx: self.adj[idx][0].v,
                   range(0, len(self.adj)))


class KruskalsMinimumSpanningTree:
    def __init__(self):
        pass

    @staticmethod
    def mst_kruskal(g):
        for v in g.get_vertices():
            DisjointSet().add(v)

        edges = []
        for lst in g.adj:
            from_node = lst[0].v
            for idx in range(1, len(lst)):
                to_node = lst[idx].v
                edges.append(Edge(lst[idx].w, from_node, to_node))

        edges.sort(key=lambda x: x.w)
        a = []
        for edge in edges:
            if DisjointSet.findSet(edge.from_node) != DisjointSet.findSet(edge.to_node):
                DisjointSet.union(edge.from_node, edge.to_node)
                a.append(edge)

        return a


def main():
    vertex_count = 9
    a = Node("a", 0)
    b = Node("b", 1)
    c = Node("c", 2)
    d = Node("d", 3)
    e = Node("e", 4)
    f = Node("f", 5)
    g = Node("g", 6)
    h = Node("h", 7)
    i = Node("i", 8)

    graph = KGraph(vertex_count)

    KGraph.add_edge(graph, a, a, 0)
    KGraph.add_edge(graph, a, b, 4)
    KGraph.add_edge(graph, a, h, 8)

    KGraph.add_edge(graph, b, b, 0)
    KGraph.add_edge(graph, b, c, 8)
    KGraph.add_edge(graph, b, h, 11)

    KGraph.add_edge(graph, c, c, 0)
    KGraph.add_edge(graph, c, d, 7)
    KGraph.add_edge(graph, c, f, 4)
    KGraph.add_edge(graph, c, i, 2)

    KGraph.add_edge(graph, d, d, 0)
    KGraph.add_edge(graph, d, e, 9)
    KGraph.add_edge(graph, d, f, 14)

    KGraph.add_edge(graph, e, e, 0)
    KGraph.add_edge(graph, e, f, 10)

    KGraph.add_edge(graph, f, f, 0)
    KGraph.add_edge(graph, f, g, 2)

    KGraph.add_edge(graph, g, g, 0)
    KGraph.add_edge(graph, g, h, 1)
    KGraph.add_edge(graph, g, i, 6)

    KGraph.add_edge(graph, h, h, 0)
    KGraph.add_edge(graph, h, i, 7)

    KGraph.add_edge(graph, i, i, 0)

    min_span_tree = KruskalsMinimumSpanningTree.mst_kruskal(graph)

    for edge in min_span_tree:
        print(edge)


if __name__ == '__main__':
    main()
