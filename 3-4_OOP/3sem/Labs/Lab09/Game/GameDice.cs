using System;

namespace Game
{
    class GameDice: GameSession
    {
        public delegate void MaxDiceEvent(); 
        public static event MaxDiceEvent MaxDiceRolled;

        Random rand;

        public GameDice()
        {
            rand = new Random();
        }

        public int Random()
        {
            int result = rand.Next(6) + 1;
            if (result == 6 && MaxDiceRolled != null) MaxDiceRolled();
            return result;
        }
    }
}
