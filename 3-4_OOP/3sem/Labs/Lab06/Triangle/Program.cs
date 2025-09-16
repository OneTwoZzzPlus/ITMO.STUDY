using System;

namespace Triangle
{
    internal class Program
    {
        static void Main(string[] args)
        {
            try
            {
                double a, b, c;
                Console.WriteLine("Введите стороны треугольника");
                Console.Write("a = "); a = double.Parse(Console.ReadLine());
                Console.Write("b = "); b = double.Parse(Console.ReadLine());
                Console.Write("c = "); c = double.Parse(Console.ReadLine());

                Triangle triangle = new Triangle(a, b, c);
                triangle.ShowLengths();
                Console.WriteLine("Периметр = {0}", triangle.Perimeter());
                Console.WriteLine("Площадь = {0}", triangle.Area());
            }
            catch (FormatException e)
            {
                Console.WriteLine("Ввод дожен содержать вещественное число. {0}", e.Message);
            }
            catch (OverflowException e)
            {
                Console.WriteLine("Слишком маленькое/большое число. {0}", e.Message);
            }
            catch (ArgumentException)
            {
                Console.WriteLine("Такого треугольника не существует =(");
            }
        }
    }
}
