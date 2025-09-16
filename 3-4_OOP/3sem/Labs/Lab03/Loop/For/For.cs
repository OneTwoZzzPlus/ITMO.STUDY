using System;

namespace For
{
    internal class For
    {
        static void Main(string[] args)
        {
            try
            {
                Console.Write("Enter k: ");
                int k = int.Parse(Console.ReadLine());
                if (k > 100 || k < 0)
                {
                    Console.WriteLine("Input must be an integer in range from 0 to 100 inc!");
                    return;
                }

                Console.Write("Enter m: ");
                int m = int.Parse(Console.ReadLine());
                if (m > 100 || m <= k)
                {
                    Console.WriteLine("Input must be an integer in range from {0} to 100 inc!", k);
                    return;
                }

                int s = 0;
                for (int i = 1; i <= 100; i++)
                {
                    if (i > k && i < m) continue;
                    s += i;
                }
                Console.WriteLine("S = {0}", s);
            }
            catch (FormatException)
            {
                Console.WriteLine("Input must be an integer in range from 0 to 100 inc!");
            }

        }
    }
}
