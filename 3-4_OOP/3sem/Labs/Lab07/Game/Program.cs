using System;

namespace Game
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Gamer g1 = new Gamer("Ivan");

            for (int i = 1; i <= 6; i++)
                Console.WriteLine("Выпало очков {0} для игрока {1}", g1.GameSession(), g1.ToString());
        }
    }
}
