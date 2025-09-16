using System;

namespace Triangle
{
    internal class Program
    {
        static void Main(string[] args)
        {
            try
            {
                Console.Write("Введите периметр: ");
                double P = Convert.ToDouble(Console.ReadLine());

                if (P <= 0)
                {
                    Console.WriteLine("Периметр должен быть положительным числом!");
                    return;
                }

                double a = P / 3;
                double p = P / 2;
                double s = Math.Sqrt(p*(p-a)*(p-a)*(p-a));

                Console.WriteLine("Сторона\tПлощадь");
                Console.WriteLine("{0:F2}\t{1:F2}", a, s);
            }
            catch (FormatException e)
            { 
                Console.WriteLine("Неккоректный ввод: {0}", e.Message);
            }
        }
    }
}
