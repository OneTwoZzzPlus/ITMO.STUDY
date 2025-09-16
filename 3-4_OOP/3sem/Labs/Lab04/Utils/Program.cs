//using System;
//namespace Utils
//{
//    internal class Program
//    {
//        static void Main(string[] args)
//        {
//            // Упражнение 1
//            Console.WriteLine("Введите первое число");
//            int x = int.Parse(Console.ReadLine());
//            Console.WriteLine("Введите второе число");
//            int y = int.Parse(Console.ReadLine());
//            int greater = Utils.Greater(x, y);
//            Console.WriteLine("Большим из чисел {0} и {1} является {2}", x, y, greater);
//        }
//    }
//}

//using System;
//namespace Utils
//{
//    internal class Program
//    {
//        static void Main(string[] args)
//        {
//            // Упражнение 2
//            Console.WriteLine("Введите первое число");
//            int x = int.Parse(Console.ReadLine());
//            Console.WriteLine("Введите второе число");
//            int y = int.Parse(Console.ReadLine());
//            Console.WriteLine("До swap: \t{0} {1}", x, y);
//            Utils.Swap(ref x, ref y);
//            Console.WriteLine("После swap: \t{0} {1}", x, y);
//        }
//    }
//}

//using System;
//namespace Utils
//{
//    internal class Program
//    {
//        static void Main(string[] args)
//        {
//            // Упражнение 3
//            int f;
//            Console.WriteLine("Число для факториала");
//            int x = int.Parse(Console.ReadLine());
//            bool ok = Utils.Factorial(x, out f);
//            if (ok)
//                Console.WriteLine("Factorial({0}) = {1}", x, f);
//            else
//                Console.WriteLine("Невозможно расчитать факториал");
//        }
//    }
//}

using System;
namespace Utils
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Упражнение 4
            Console.Write("Треугольник равносторонний? ['+' - да, иначе - нет]: ");
            string ans = Console.ReadLine();
            if (ans == "+")
            {
                Console.WriteLine("Введите длину стороны");
                int a = int.Parse(Console.ReadLine());

                double s = Operation.Area(a);
                Console.WriteLine("Площадь равностороннего треугольника равна {0:f4}", s);
            }
            else
            {
                Console.WriteLine("Введите длину стороны A");
                int a = int.Parse(Console.ReadLine());
                Console.WriteLine("Введите длину стороны B");
                int b = int.Parse(Console.ReadLine());
                Console.WriteLine("Введите длину стороны C");
                int c = int.Parse(Console.ReadLine());

                double s = Operation.Area(a, b, c);
                Console.WriteLine("Площадь треугольника равна {0:f4}", s);
            }
        }
    }
}

//using System;
//namespace Utils
//{
//    internal class Program
//    {
//        static void Main(string[] args)
//        {
//            // Упражнение 5
//            bool ok;
//            Console.WriteLine("Решатель a*x^2 + b*x + c = 0");
//            Console.WriteLine("Введите a");
//            ok = double.TryParse(Console.ReadLine(), out double a);
//            if (!ok)
//            {
//                Console.WriteLine("Разрешены только double через десятичную запятую!");
//                return;
//            }
//            Console.WriteLine("Введите b");
//            ok = double.TryParse(Console.ReadLine(), out double b);
//            if (!ok)
//            {
//                Console.WriteLine("Разрешены только double через десятичную запятую!");
//                return;
//            }
//            Console.WriteLine("Введите c");
//            ok = double.TryParse(Console.ReadLine(), out double c);
//            if (!ok)
//            {
//                Console.WriteLine("Разрешены только double через десятичную запятую!");
//                return;
//            }

//            int res = Solver.QuadraticEquation(a, b, c, out double x1, out double x2);
//            switch (res)
//            {
//                case -1:
//                    Console.WriteLine("Корней уравнения с коэффициентами a = {0}, b = {1}, c = {2} нет.", 
//                        a, b, c);
//                    break;
//                case 0:
//                    Console.WriteLine("Корень уравнения с коэффициентами a = {0}, b = {1}, c = {2} один x1=x2={3}.", 
//                        a, b, c, x1);
//                    break;
//                case 1:
//                    Console.WriteLine("Корни уравнения с коэффициентами a = {0}, b = {1}, c = {2} равны x1={3}, x2={4}.", 
//                        a, b, c, x1, x2);
//                    break;
//            }

//        }
//    }
//}
