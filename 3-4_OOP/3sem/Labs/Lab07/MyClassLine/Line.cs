using System;

namespace MyClassLine
{
    class Line
    {
        private Point pStart;
        private Point pEnd;

        public Line() { }
        public Line(Point pStart, Point pEnd)
        {
            this.pStart = pStart;
            this.pEnd = pEnd;
        }
        public void Show()
        {
            Console.WriteLine("Отрезок с координатами: ({0}) - ({1})", pStart, pEnd);
        }
        public double Length()
        {
            return pStart.Length(pEnd);
        }
    }
}
