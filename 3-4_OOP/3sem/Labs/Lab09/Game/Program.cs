using System;

namespace Game
{
    internal class Program
    {
        static void MaxResult()
        {
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("Выпало максимальное количество очков!");
            Console.ResetColor();
        }

        static void Main(string[] args)
        {
            GameDice.MaxDiceRolled += MaxResult;
            Gamer g1 = new Gamer("Ivan");

            for (int i = 1; i <= 10; i++)
                Console.WriteLine("Выпало очков {0} для игрока {1}", g1.GameSession(), g1.ToString());
        }
    }
}
