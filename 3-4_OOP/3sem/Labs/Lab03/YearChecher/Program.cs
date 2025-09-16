using System;

namespace YearChecher
{
    internal class Program
    {
        static void Main(string[] args)
        {
            try
            {
                Console.Write("Enter year number: ");
                int year = int.Parse(Console.ReadLine());

                if (year <= 0)
                {
                    Console.WriteLine("Positive integer!");
                    return;
                }


                if (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0))
                    Console.WriteLine("YES");
                else
                    Console.WriteLine("NO");
            } 
            catch (FormatException)
            {
                Console.WriteLine("Input must be a positive integer");
            }
        }
    }
}
