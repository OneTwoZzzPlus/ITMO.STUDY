/* number 30 - variant 2 */
using System;

namespace ShootingMain
{
    internal class ShootingMain
    {
        static void Main(string[] args)
        {
            try {
                Console.Write("Введите количество выстрелов: ");
                int shotsCount = int.Parse(Console.ReadLine());
                if (shotsCount <= 0)
                {
                    Console.WriteLine("Должно быть положительное число!");
                    return;
                }

                int totalScore = 0;
                int i = 0;
                while (i < shotsCount)
                {
                    try
                    {
                        Console.Write("Введите X выстрела {0}: ", i + 1);
                        double x = double.Parse(Console.ReadLine());
                        Console.Write("Введите Y выстрела {0}: ", i + 1);
                        double y = double.Parse(Console.ReadLine());

                        double radius = x * x + y * y;
                        if (radius <= 1)
                            totalScore += 10;
                        else if (radius <= 4)
                            totalScore += 5;
                        else if (radius <= 9)
                            totalScore += 1;

                        i++;
                    }
                    catch (FormatException e) 
                    {
                        Console.WriteLine("Некорректная координата: {0}", e.Message);
                    }
                    catch (OverflowException e)
                    {
                        Console.WriteLine("Слишком большая координата: {0}", e.Message);
                    }
                }

                Console.WriteLine("Сумма очков: {0}", totalScore);
            }
            catch (FormatException e)
            {
                Console.WriteLine("Должно быть положительное целое число: {0}", e.Message);
            }
            catch (OverflowException e)
            {
                Console.WriteLine("Слишком большое число: {0}", e.Message);
            }
        }
    }
}
