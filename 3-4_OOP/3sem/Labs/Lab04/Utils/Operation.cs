using System;

namespace Utils
{
    internal class Operation
    {
        private static bool IsRealTriangle(double a, double b, double c)
        {
            return a + b > c && a + c > b && b + c > a && a > 0 && b > 0 && c > 0;
        }
        public static double Area(double a, double b, double c)
        {
            if (!IsRealTriangle(a, b, c)) throw new Exception("Такого треугольника не существует!");

            double p = (a + b + c) / 2;
            return Math.Sqrt(p * (p - a) * (p - b) * (p - c)); ;
        }

        public static double Area(double a)
        {
            if (a <= 0) throw new Exception("Такого треугольника не существует!");

            return Math.Sqrt(3) / 4 * a * a;
        }
    }
}
