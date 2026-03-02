using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Graphs
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //Graph g1 = new Graph(6, false, 1, 1);
            //g1.Print();
            //g1.DFS(0);
            //g1.BFS(0);

            //Graph g2 = new Graph(6, true, 1, 9);
            //g2.Print();
            //g2.Dejkstra(0);

            //UnorderedGraph g3 = new UnorderedGraph(6, 1, 21);
            //g3.Print();
            //g3.Kruskal();

            //UnorderedGraph gza = new UnorderedGraph(new int[8][] {
            //    new int[8] {0, 19, 0, 0, 0, 25, 0, 6},
            //    new int[8] {19, 0, 9, 0, 0, 0, 0, 0},
            //    new int[8] {0, 9, 0, 14, 0, 0, 0, 0},
            //    new int[8] {0, 0, 14, 0, 21, 2, 0, 0},
            //    new int[8] {0, 0, 0, 21, 0, 0, 0, 0},
            //    new int[8] {25, 0, 0, 2, 0, 0, 8, 11},
            //    new int[8] {0, 0, 0, 0, 0, 8, 0, 17},
            //    new int[8] {6, 0, 0, 0, 0, 11, 17, 0}
            //});
            //gza.Print();
            //gza.Kruskal();

            UnorderedGraph gzb = new UnorderedGraph(new int[9][] {
                new int[9] {0, 2, 0, 3, 5, 0, 0, 0, 0},
                new int[9] {2, 0, 10, 0, 0, 0, 0, 0, 0},
                new int[9] {0, 10, 0, 0, 4, 0, 0, 5, 6},
                new int[9] {3, 0, 0, 0, 0, 8, 0, 0, 0},
                new int[9] {5, 0, 2, 0, 0, 7, 0, 0, 0},
                new int[9] {0, 0, 0, 8, 7, 0, 4, 3, 0},
                new int[9] {0, 0, 0, 0, 0, 4, 0, 0, 11},
                new int[9] {0, 0, 5, 0, 0, 3, 0, 0, 0},
                new int[9] {0, 0, 6, 0, 0, 0, 11, 0, 0}
            });
            gzb.Print();
            gzb.Kruskal();
        }
    }
}
