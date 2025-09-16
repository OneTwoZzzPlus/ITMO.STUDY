using System;

namespace Greetings
{
    internal class Greeter
    {
        static void Main()
        {
            string name;
            Console.WriteLine("Please enter your name");
            name = Console.ReadLine();
            Console.WriteLine("Hello, {0}", name);
        }
    }
}
