import add_path
import mit_ocw_data_science.lec3.lecture3_graph as lec3
import pytest

class TestDigraph:
    def setup_method(self):
        self.graph = lec3.Digraph()
        self.node1 = lec3.Node('1')
        self.node2 = lec3.Node('2')
        self.node3 = lec3.Node('3')
        self.edge1 = lec3.Edge(self.node1, self.node2)
        self.edge2 = lec3.Edge(self.node2, self.node3)

    def test_add_node(self):
        self.graph.add_node(self.node1)
        assert self.graph.has_node(self.node1)
        assert not self.graph.has_node(self.node2)
        self.graph.add_node(self.node2)
        assert self.graph.has_node(self.node2)
    def test_add_edge(self):
        self.graph.add_node(self.node1)
        self.graph.add_edge(lec3.Edge(self.node3, lec3.Node('4')))
        assert lec3.Node('4') in self.graph.children_of(self.node3)
        assert not self.graph.has_edge(self.edge1)
        self.graph.add_edge(self.edge1)