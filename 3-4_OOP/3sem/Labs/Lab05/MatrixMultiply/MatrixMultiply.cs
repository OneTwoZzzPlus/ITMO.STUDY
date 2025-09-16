using System;
namespace MatrixMultiply
{
    internal class MatrixMultiply
    {
        static void Main(string[] args)
        {
            int[,] a = new int[2, 2];
            Input(a);
            int[,] b = new int[2, 2];
            Input(b);
            int[,] result = Multiply(a, b);

            Output(result);
        }
        private static void Input(int[,] a)
        {
            for (int r = 0; r < a.GetLength(0); r++)
            {
                for (int c = 0; c < a.GetLength(1); c++)
                {
                    Console.Write("Enter value for [{0}, {1}] : ", r, c);
                    a[r, c] = int.Parse(Console.ReadLine());
                }
            }
            Console.WriteLine();
        }
        private static int[,] Multiply(int[,] a, int[,] b)
        {
            int[,] result = new int[2, 2];
            for (int r = 0; r < result.GetLength(0); r++)
            {
                for (int c = 0; c < result.GetLength(1); c++)
                {
                    result[r, c] += a[r, 0] * b[0, c] + a[r, 1] * b[1, c];
                }
            }
            return result;
        }
        private static void Output(int[,] result)
        {
            for (int r = 0; r < result.GetLength(0); r++)
            {
                for (int c = 0; c < result.GetLength(1); c++)
                {
                    Console.Write("{0} ", result[r, c]);
                }
                Console.WriteLine();
            }
        }
    }
}
