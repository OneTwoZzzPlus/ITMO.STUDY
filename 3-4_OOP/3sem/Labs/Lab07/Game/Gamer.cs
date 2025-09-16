namespace Game
{
    class Gamer
    {
        string Name;
        GameDice Session;

        public Gamer(string name)
        {
            Name = name;
            Session = new GameDice();
        }

        public int GameSession()
        {
            return Session.random();
        }

        public override string ToString()
        {
            return Name;
        }
    }
}
