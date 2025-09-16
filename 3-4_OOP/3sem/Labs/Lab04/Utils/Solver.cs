using System;

namespace Utils
{
    internal class Solver
    {
        public static int QuadraticEquation(double a, double b, double c, out double x1, out double x2)
        {
            if (a == 0 && b == 0)
            {
                x1 = 0;
                x2 = 0;
                return -1;
            }
            if (a == 0)
            {
                x1 = -c / b;
                x2 = -c / b;
                return 0;
            }

            double D = b * b - 4 * a * c;
            if (D < 0)
            {
                x1 = 0;
                x2 = 0;
                return -1;
            }
            else if (D == 0)
            {
                x1 = -b / (2 * a);
                x2 = -b / (2 * a);
                return 0;
            }
            else
            {
                x1 = (-b + Math.Sqrt(D)) / (2 * a);
                x2 = (-b - Math.Sqrt(D)) / (2 * a);
                return 1;
            }
        }
    }
}
