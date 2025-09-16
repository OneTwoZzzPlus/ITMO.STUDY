using System;
namespace Progressions
{
    class GeometricProgression: Progression
    {
        private double first;
        private double denominator;

        public GeometricProgression(double first, double denominator)
        {
            this.first = first;
            this.denominator = denominator;
        }

        public double GetElement(int k)
        {
            if (k <= 0) throw new ArgumentOutOfRangeException();
            return first * Math.Pow(denominator, k - 1);
        }
    }
}
