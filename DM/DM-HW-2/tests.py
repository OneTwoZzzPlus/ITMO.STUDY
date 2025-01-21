import sys
import os
import unittest


PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PATH)


from graph import Graph, InvalidGraph


class TestGraph(unittest.TestCase):

    def test_invalid_graphs(self):
        empty_graph = []

        wrong_type_input = "[[0, 1], [1, 0]]"

        wrong_type_row = [[1, 2], (2, 1)]

        wrong_type_cell = [[1, 2], [1, '2']]

        not_constant_rows_length = [[1, 2], [1, 2, 3]]

        not_square_table = [[1, 2], [1, 2], [1, 2]]

        self.assertRaises(InvalidGraph, Graph, wrong_type_input)
        self.assertRaises(InvalidGraph, Graph, wrong_type_row)
        self.assertRaises(InvalidGraph, Graph, wrong_type_cell)
        self.assertRaises(InvalidGraph, Graph, empty_graph)
        self.assertRaises(InvalidGraph, Graph, not_constant_rows_length)
        self.assertRaises(InvalidGraph, Graph, not_square_table)

    def test_directed_graphs(self):
        graph1 = Graph([
            [0, 18, 13, 0,  7, 0],
            [0, 0,  10, 12, 0, 0],
            [0, 0,  0,  0,  19, 0],
            [0, 4,  9,  0,  0, 20],
            [0, 0,  8,  7,  0, 4],
            [0, 0,  0,  0,  0, 0]
        ])

        self.assertEqual(graph1.EdmondsKarp(0, 5), 23)
        self.assertEqual(graph1.FordFulkerson(0, 5), 23)

        graph2 = Graph([
            [0, 7, 4, 0,  0, 0],
            [0, 0,  4, 0, 2, 0],
            [0, 0,  0,  4, 8, 0],
            [0, 0,  0,  0,  0, 12],
            [0, 0,  0,  4,  0, 5],
            [0, 0,  0,  0,  0, 0]
        ])

        self.assertEqual(graph2.EdmondsKarp(0, 5), 10)
        self.assertEqual(graph2.FordFulkerson(0, 5), 10)
        

    def test_undirected_graphs(self):
        graph = Graph([
            [0, 6, 0],
            [6, 0, 3],
            [0, 3, 0]
        ])

        self.assertEqual(graph.EdmondsKarp(0, 2), 3)
        self.assertEqual(graph.FordFulkerson(0, 2), 3)

    def test_same_weighted_graphs(self):
        graph1 = Graph([
            [0, 1, 1, 0],
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [0, 1, 1, 0]
        ])

        self.assertEqual(graph1.EdmondsKarp(0, 3), 1)
        self.assertEqual(graph1.FordFulkerson(0, 3), 1)

        graph2 = Graph([
            [0, 1, 1, 0],
            [1, 0, 1, 1],
            [0, 1, 0, 1],
            [1, 0, 1, 0]
        ])

        self.assertEqual(graph2.EdmondsKarp(0, 3), 2)
        self.assertEqual(graph2.FordFulkerson(0, 3), 2)

    def test_disconnected_graphs(self):
        graph = Graph([
            [0, 1,  2,  0,  0, 0],
            [10, 0,  3,  0,  0, 0],
            [4, 2,  0,  0,  0, 0],
            [0, 0,  0,  0,  1, 1],
            [0, 0,  0,  0,  0, 1],
            [0, 0,  0,  1,  0, 0]
        ])

        self.assertEqual(graph.EdmondsKarp(0, 2), 3)
        self.assertEqual(graph.FordFulkerson(0, 2), 3)

        self.assertEqual(graph.EdmondsKarp(3, 5), 2)
        self.assertEqual(graph.FordFulkerson(3, 5), 2)

    def test_cyclic_graphs(self):
        graph = Graph([
            [0, 1, 6, 3],
            [0, 0, 0, 2],
            [5, 1, 0, 5],
            [0, 0, 5, 0]
        ])

        self.assertEqual(graph.EdmondsKarp(0, 3), 10)
        self.assertEqual(graph.FordFulkerson(0, 3), 10)

    def test_acyclic_graphs(self):
        graph = Graph([
            [0, 7, 4, 0,  0, 0],
            [0, 0,  4, 0, 2, 0],
            [0, 0,  0,  4, 8, 0],
            [0, 0,  0,  0,  0, 12],
            [0, 0,  0,  0,  0, 5],
            [0, 0,  0,  0,  0, 0]
        ])

        self.assertEqual(graph.EdmondsKarp(0, 5), 9)
        self.assertEqual(graph.FordFulkerson(0, 5), 9)


if __name__ == "__main__":
    unittest.main()