using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.ExceptionServices;


namespace Graphs
{
    public class Graph
    {
        protected static Random rand = new Random();
        public int n { get; protected set; }
        public int[][] g;
        private int min_val = 0, max_val = int.MaxValue;

        public List<int> used = new List<int>();
        public Queue<int> queue = new Queue<int>();

        public bool[] viewed;
        public int[] len;
        public int[] next;


        public Graph(int[][] gr)
        {
            n = gr.Count();
            g = gr;
        }

        protected Graph(int size)
        {
            n = size;
            g = new int[n][];
            for (int i = 0; i < n; i++) g[i] = new int[n];
        }

        public Graph(int size, bool oriented, int min_value = 0, int max_value = int.MaxValue - 1) : this(size)
        {
            min_val = min_value;
            max_val = max_value;
            
            if (oriented)
            {
                for (int i = 0; i < n; i++)
                {
                    for (int j = 0; j < n; j++)
                    {
                        if (i == j) continue;
                        int r = rand.Next(0, 2) == 1 ? rand.Next(min_value, max_value + 1) : 0;
                        g[i][j] = r;
                    }
                }
            }
            else
            {
                for (int i = 0; i < n; i++)
                {
                    for (int j = i + 1; j < n; j++)
                    {
                        int r = rand.Next(0, 2) == 1 ? rand.Next(min_value, max_value + 1) : 0;
                        g[i][j] = r;
                        g[j][i] = r;
                    }
                }
            }
        }

        public override string ToString()
        {
            string s = "\nGraph";
            for (int i = 0; i < n; i++)
            {
                s += "\nNode " + i + " : [" + string.Join((max_val > 9 ? " " : ""), g[i]) + "]";
            }
            return s;
        }

        public void Print()
        {
            Console.WriteLine(ToString());
        }

        public void DFS(int i, bool first = true)
        {
            if (first)
            {
                Console.WriteLine("\nDFS");
                used = new List<int>();
            }

            Console.WriteLine(" Node {0}", i);
            Console.WriteLine("Used: [{0}]", string.Join(", ", used));

            used.Add(i);
            for (int j = 0; j < n; j++)
            {
                if (g[i][j] == 1 && !used.Contains(j))
                {
                    DFS(j, false);
                }
            }
        }

        public void BFS(int i, bool first = true)
        {
            if (first)
            {
                Console.WriteLine("\nBFS");
                used = new List<int>();
                queue = new Queue<int>();
            }

            Console.WriteLine(" Node {0}", i);
            Console.WriteLine("Used: [{0}]", string.Join(", ", used));
            Console.WriteLine("Queue: [{0}]", string.Join(", ", queue));

            used.Add(i);
            for (int j = 0; j < n; j++)
            {
                if (g[i][j] == 1 && !used.Contains(j) && !queue.Contains(j))
                {
                    queue.Enqueue(j);
                }
            }

            if (queue.Count() != 0) BFS(queue.Dequeue(), false);
        }

        public void Dejkstra(int i, bool first = true)
        {
            if (first)
            {
                if (min_val < 0) throw new Exception("Negative weighted edges not allowed");
                viewed = new bool[n];
                len = new int[n];
                next = new int[n];
                for (int j = 0; j < n; j++)
                {
                    viewed[j] = false;
                    len[j] = int.MaxValue;
                    next[j] = -1;
                }
                len[i] = 0;
            }

            viewed[i] = true;

            int minDist = int.MaxValue;
            int minVertex = -1;
            for (int j = 0; j < n; j++)
            {
                if (g[i][j] != 0 && !viewed[j] && len[i] != int.MaxValue)
                {
                    int newLen = len[i] + g[i][j];
                    if (newLen < len[j])
                    {
                        len[j] = newLen;
                        next[j] = i;
                    }
                }

                if (!viewed[j] && len[j] < minDist)
                {
                    minDist = len[j];
                    minVertex = j;
                }
            }

            if (minVertex != -1) Dejkstra(minVertex, false);

            if (first) PrintPaths(i);
        }

        public void PrintPaths(int i)
        {
            Console.WriteLine("\n");
            for (int j = 1; j < n; j++)
            {
                if (i == j) continue;

                Console.WriteLine("Path to {1} from {0} (len={2}):", 0, j, (len[j] == int.MaxValue) ? "inf" : len[j].ToString());

                int z = j;
                while (z != 0 && z != -1)
                {
                    Console.Write(z + " <- ");
                    z = next[z];
                }
                if (z == -1) Console.WriteLine("no way");
                else Console.WriteLine(z);
            }
        }

    }
}
