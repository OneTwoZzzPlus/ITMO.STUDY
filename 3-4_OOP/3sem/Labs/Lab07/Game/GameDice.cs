using System;

namespace Game
{
    class GameDice
    {
        Random rand;

        public GameDice()
        {
            rand = new Random();
        }

        public int random()
        {
            return rand.Next(6) + 1;
        }
    }
}
