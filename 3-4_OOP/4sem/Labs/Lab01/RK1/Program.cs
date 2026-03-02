using System;
using System.Collections.Generic;

namespace RK1
{
    internal class Program
    {

        static void Main(string[] args)
        {
            int p = 31;

            // Input n - count of words
            int n = 0;
            Console.Write("Write n = ");
            while (!int.TryParse(Console.ReadLine(), out n))
            {
                Console.Write("Must be positive int! Write n = ");
            }

            // Input words
            Console.WriteLine("Input strings:");
            string[] strings = new string[n];
            int m = 0;
            for (int i = 0; i < n; i++)
            {
                strings[i] = Console.ReadLine();
                if (strings[i].Length > m) m = strings[i].Length;
            } 
            
            // Calculate powers
            int[] p_pow = new int[m];
            p_pow[0] = 1;
            for (int i = 1; i < m; i++)
            {
                p_pow[i] = p_pow[i - 1] * p;
            }

            // Collect groups
            Dictionary<int, List<int>> groups = new Dictionary<int, List<int>>();
            for (int i = 0; i < n; i++)
            {
                int hash = 0;
                for (int j = 0; j < strings[i].Length; j++)
                {
                    hash += (strings[i][j] - 'a' + 1) * p_pow[j];
                }

                if (!groups.ContainsKey(hash)) groups[hash] = new List<int>();

                groups[hash].Add(i);
            }

            // Output
            int n_group = 1;
            Console.WriteLine("\nGroups (n = {0}, m = {1}, p = {2})", n, m, p);
            foreach (var group in groups)
            {
                Console.WriteLine(
                    "Group {0}: {1}", 
                    n_group++, 
                    string.Join(" ", group.Value)
                );
            }
        }
    }
}
