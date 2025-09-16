using System;

namespace Loop
{
    internal class DoWhile
    {
        static void Main(string[] args)
        {
            double x, x1, x2, y;

            Console.Write("Enter x1: ");
            x1 = double.Parse(Console.ReadLine());
            Console.Write("Enter x2: ");
            x2 = double.Parse(Console.ReadLine());

            Console.WriteLine("x\t| sin(x)");
            x = x1;
            do
            {
                y = Math.Sin(x);
                Console.WriteLine("{0:f2}\t|{1:f4}", x, y);
                x += 0.01;
            }
            while (x <= x2);
        }
    }
}
