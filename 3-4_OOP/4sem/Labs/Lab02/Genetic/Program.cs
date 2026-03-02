using System;
using System.Collections.Generic;
using System.Linq;

namespace Genetic
{
    internal class Program
    {
        public static Random r = new Random();
        public static int res = 30;
        public static int n = 4;
        public static Func<int[], int> f = (a) => a[0] + 2 * a[1] + 3 * a[2] + 2 * a[3];

        static void Main(string[] args)
        {
            List<Generation> generations = new List<Generation>();
            for (int i = 0; i < 5; i++)
            {
                int[] newArgs = { r.Next(1, 31), r.Next(1, 31), r.Next(1, 31), r.Next(1, 31) };
                generations.Add(new Generation(f, newArgs, res));
            }

            for (int i = 0; i<1000; i++)
            {
                Console.WriteLine("Iteration {0}", i + 1);
                for (int j = 0; j < n; j++)
                {
                    Console.WriteLine("Gen {0}: {1}", j + 1, string.Join(" ", generations[j].args));
                }

                double koef1 = Generation.SurvivalKoef(generations);
                var best = generations.OrderBy(g => g.GetAc()).ToList();
                foreach (Generation gen in generations)
                {
                    if (gen.RealResult == res)
                    {
                        Console.WriteLine("Solution");
                        Console.WriteLine(string.Join(" ", gen.args));
                        return;
                    }
                    generations = new List<Generation> { 
                        best[0] + best[1], best[1] + best[0], best[0] + best[2],
                        best[2] + best[0], best[1] + best[2]};
                    double koef2 = Generation.SurvivalKoef(generations);
                    if (koef2 <= koef1)
                    {
                        int x = r.Next(1, 5);
                        for (int j = 0; j < x; j++)
                        {
                            generations[r.Next(0, n)].Mutation();
                        }
                    }
                }
            }
        }
    }
}
