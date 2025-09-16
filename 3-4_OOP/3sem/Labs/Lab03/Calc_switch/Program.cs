using System;

namespace Calc_switch
{
    internal class Program
    {
        static void Main(string[] args)
        {
            try
            {
                Console.Write("A = ");
                double a = double.Parse(Console.ReadLine());
                Console.Write("OP = ");
                char op = char.Parse(Console.ReadLine());
                Console.Write("B = ");
                double b = double.Parse(Console.ReadLine());

                bool ok = true;
                double res = 0;

                switch (op)
                {
                    case '+': res = a + b; break;
                    case '-': res = a - b; break;
                    case '*': res = a * b; break;
                    case '/': res = a / b; break;
                    default: ok = false; break;
                }

                if (ok)
                    Console.WriteLine("{0} {1} {2} = {3}", a, op, b, res);
                else
                    Console.WriteLine("Операция не определена");
            }
            catch (DivideByZeroException)
            {
                Console.WriteLine("Деление на ноль не определено");
            }
            catch (FormatException)
            {
                Console.WriteLine("Некорректный ввод");
            }
        }
    }
}
