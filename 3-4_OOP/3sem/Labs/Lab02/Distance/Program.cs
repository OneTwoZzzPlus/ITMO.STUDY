using System;

namespace Distance
{
    public struct Distance
    {
        public uint foot;
        public byte inch;
    }

    internal class Program
    {
        static void Main(string[] args)
        {
            try
            {
                uint temp;
                Distance distanceA, distanceB, distanceC;

                Console.Write("Enter A distance in inches (positive integer): ");
                temp = uint.Parse(Console.ReadLine());
                distanceA.foot = temp / 12;
                distanceA.inch = (byte)(temp % 12);

                Console.Write("Enter B distance in inches (positive integer): ");
                temp = uint.Parse(Console.ReadLine());
                distanceB.foot = temp / 12;
                distanceB.inch = (byte)(temp % 12);

                distanceC.foot = (uint)(distanceA.foot + distanceB.foot + (distanceA.inch + distanceB.inch) / 12);
                distanceC.inch = (byte)((distanceA.inch + distanceB.inch) % 12);

                Console.WriteLine("{0}' - {1}\"", distanceC.foot, distanceC.inch);
            }
            catch (FormatException e)
            {
                // Catch non-digit input
                Console.WriteLine("Input must be a positive integer!");
            }
            catch (OverflowException e)
            {
                // Catch negative and overflow values
                Console.WriteLine("Input must be in range from 0 to {0} inc!", uint.MaxValue);
            }
            
        }
    }
}
