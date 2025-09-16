using System;

namespace Progressions
{
    internal class Program
    {
        static void Main(string[] args)
        {
            try
            {
                Console.Write("Выберите вид прогрессии ['+' - арифмет., иначе - геометр.]: ");
                string type = Console.ReadLine();
                bool arifmet = type == "+";
                Console.Write("Введите первый элемент: ");
                double first = double.Parse(Console.ReadLine());
                Console.Write("Введите {0}: ", arifmet ? "разность" : "множитель");
                double d = double.Parse(Console.ReadLine());
                Console.Write("Введите номер элемента: ");
                int k = int.Parse(Console.ReadLine());

                Progression progression;
                if (arifmet)
                    progression = new ArithmeticProgression(first, d);
                else
                    progression = new GeometricProgression(first, d);
                Console.WriteLine("Элемент номер {0} равен {1}", k, progression.GetElement(k));
            }
            catch (FormatException)
            {
                Console.WriteLine("Некорректный ввод.");
            }
            catch (OverflowException e)
            {
                Console.WriteLine("Слишком маленькое/большое число. {0}", e.Message);
            }
            catch (ArgumentOutOfRangeException)
            {
                Console.WriteLine("Номер элемента должен быть положительным числом!");
            }
        }
    }
}
