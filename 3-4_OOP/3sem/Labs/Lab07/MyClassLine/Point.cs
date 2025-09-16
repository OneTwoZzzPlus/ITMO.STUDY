using System;

namespace MyClassLine
{
    class Point
    {
        private double x;
        private double y;

        public Point() { }
        public Point(double x, double y)
        {
            this.x = x;
            this.y = y;
        }
        public void Show()
        {
            Console.WriteLine("Точка с координатами: ({0}, {1})", x, y);
        }
        public double Length(Point p)
        {
            return Math.Sqrt(Math.Pow(this.x - p.x, 2) + Math.Pow(this.y - p.y, 2));
        }
        public override string ToString()
        {
            return x + ", " + y;
        }
    }
}
