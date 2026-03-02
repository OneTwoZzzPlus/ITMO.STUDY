using System;

namespace RK2
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Input
            int p = 31;
            Console.Write("s = ");
            string s = Console.ReadLine();
            Console.Write("t = ");
            string t = Console.ReadLine();
            int n = s.Length;
            int m = t.Length;

            // Calculate powers
            int[] p_pow = new int[m];
            p_pow[0] = 1;
            for (int i = 1; i < m; i++)
            {
                p_pow[i] += p_pow[i - 1] * p;
            }

            // Hash of s
            int s_hash = 0;
            for (int i = 0; i < n; i++)
            {
                s_hash += (s[i] - 'a' + 1) * p_pow[i];
            }

            // Prefix hashs of t
            int[] t_hashs = new int[m];
            for (int i = 0; i < m; i++)
            {
                t_hashs[i] += (t[i] - 'a' + 1) * p_pow[i];
                if (i != 0) t_hashs[i] += t_hashs[i - 1];
            }

            // Find s in t
            int current_hash = 0;
            for (int i = 0; (i + n - 1) < m; i++)
            {
                current_hash = t_hashs[i + n - 1];
                if (i != 0) current_hash -= t_hashs[i - 1];
                if (current_hash == s_hash * p_pow[i])
                {
                    Console.WriteLine(i);
                }

            }

        }
    }
}
