using System;

namespace Triangle
{
    internal class Triangle
    {
        private double a;
        private double b;
        private double c;

        public Triangle(double a, double b, double c)
        {
            this.a = a; 
            this.b = b; 
            this.c = c;
            if (!IsReal()) throw new ArgumentException("Triangle is not real!"); 
        }

        public void ShowLengths()
        {
            Console.WriteLine("Длины сторон треугольника: a = {0}, b = {1}, c = {2}", a, b, c);
        }

        public double Perimeter()
        {
            return a + b + c;
        }
        public double Area()
        {
            double p = (a + b + c) / 2;
            return Math.Sqrt(p * (p - a) * (p - b) * (p - c));
        }

        public bool IsReal()
        {
            return a > 0 && b > 0 && c > 0 && (a + b) > c && (a + c) > b && (b + c) > a;
        }
    }
}
