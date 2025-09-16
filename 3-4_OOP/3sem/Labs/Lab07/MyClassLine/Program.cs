using System;

namespace MyClassLine
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Point p1 = new Point(2, 3);
            Point p2 = new Point(-1, -2);
            p1.Show();
            p2.Show();

            Line line = new Line(p1, p2);
            line.Show();

            Console.WriteLine("Длина отрезка {0}", line.Length());
        }
    }
}
