using System;
using System.Collections.Generic;
using System.ComponentModel;

namespace Graphs
{
    public class UnorderedGraph : Graph
    {
        public List<Edge> reb = new List<Edge>();

        public UnorderedGraph(int[][] gr) : base(gr) {
            for (int i = 0; i < n; i++)
            {
                for (int j = i + 1; j < n; j++)
                {
                    if (g[i][j] != 0)
                    {
                        Edge edge = new Edge(i, j, g[i][j]);
                        reb.Add(edge);
                    }
                }
            }
        }
        public UnorderedGraph(int size, int min_value = 0, int max_value = int.MaxValue - 1) : base(size, false, min_value, max_value) {
            for (int i = 0; i < n; i++)
            {
                for (int j = i + 1; j < n; j++)
                {
                    if (g[i][j] != 0)
                    {
                        Edge edge = new Edge(i, j, g[i][j]);
                        reb.Add(edge);
                    }
                }
            }
        }

        public void Kruskal()
        {
            reb.Sort((a, b) => a.Weight.CompareTo(b.Weight));

            List<Edge> mst = new List<Edge>();
            List<HashSet<int>> components = new List<HashSet<int>>();

            foreach (Edge edge in reb)
            {
                if (edge.Check(components))
                {
                    mst.Add(edge);
                }
            }

            Console.WriteLine("\nMinimum Spanning Tree (Kruskal):");
            int totalWeight = 0;
            foreach (Edge edge in mst)
            {
                Console.WriteLine(edge);
                totalWeight += edge.Weight;
            }
            Console.WriteLine($"Total weight: {totalWeight}");
        }
    }
}
