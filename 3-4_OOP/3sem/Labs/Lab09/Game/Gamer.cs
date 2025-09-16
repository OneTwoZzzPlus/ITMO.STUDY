namespace Game
{
    class Gamer
    {
        string Name;
        GameSession Session;

        public Gamer(string name)
        {
            Name = name;
            Session = new GameDice();
        }

        public Gamer(string name, GameSession session)
        {
            Name = name;
            Session = session;
        }

        public int GameSession()
        {
            return Session.Random();
        }

        public override string ToString()
        {
            return Name;
        }
    }
}
