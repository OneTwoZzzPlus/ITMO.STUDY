using System;
namespace Progressions
{
    class ArithmeticProgression : Progression
    {
        private double first;
        private double difference;

        public ArithmeticProgression(double first, double difference)
        {
            this.first = first;
            this.difference = difference;
        }

        public double GetElement(int k)
        {
            if (k <= 0) throw new ArgumentOutOfRangeException();
            return first + difference * (k - 1);
        }
    }
}
